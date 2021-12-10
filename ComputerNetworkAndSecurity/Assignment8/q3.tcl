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

$ns duplex-link $n0 $n2 5Mb 10ms DropTail
$ns duplex-link $n1 $n2 5Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail


$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right

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

# UDP
set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0

#CBR
set cbr0 [new Application/Traffic/CBR]
$cbr0 set ret_ 448kb

$cbr0 attach-agent $udp0

set null0 [new Agent/Null]
$ns attach-agent $n3 $null0

# UDP should be connected with all agents and applications so connecting
$ns connect $udp0 $null0

# simulating
$ns at 1.0 "$ftp start"
$ns at 1.0 "$cbr0 start"
$ns at 4.0 "$ftp stop"
$ns at 4.0 "$cbr0 stop"

$ns at 5.0 "finish"

$ns run
