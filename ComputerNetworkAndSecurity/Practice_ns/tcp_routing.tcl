set ns [new Simulator]

$ns color 1 Blue

set nf [open out.nam w]
$ns namtrace-all $nf

set nf1 [open out.tr w]
$ns trace-all $nf1

proc finish {} {
    global ns nf nf1
    $ns flush-trace
    close $nf
    close $nf1
    exec nam out.nam &
    exit 0
}

set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]

$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.7Mb 20ms DropTail

#  How many packet can be hold by n2 i.e.10
$ns queue-limit $n2 $n3 10

$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right

$ns duplex-link-op $n2 $n3 queuePos 0.5

set tcp [new Agent/TCP]
$tcp set class_ 2

$ns attach-agent $n0 $tcp

set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink

$ns connect $tcp $sink
$tcp set fid_ 1

# file transfer protocol

set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP

# simulating
$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"

$ns at 5.0 "finish"

$ns run
