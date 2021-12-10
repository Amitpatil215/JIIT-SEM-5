set ns [new Simulator]

$ns color 1 Blue
$ns color 2 Red

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
set n4 [$ns node]

$ns duplex-link $n0 $n4 5Mb 15ms DropTail
$ns duplex-link $n1 $n4 5Mb 20ms DropTail
$ns duplex-link $n3 $n4 2Mb 10ms DropTail
$ns duplex-link $n2 $n4 1Mb 20ms DropTail

$ns duplex-link-op $n0 $n4 orient right
$ns duplex-link-op $n1 $n4 orient down
$ns duplex-link-op $n3 $n4 orient up
$ns duplex-link-op $n2 $n4 orient left

#tcp 0
set tcp0 [new Agent/TCP]
$tcp0 set class_ 1

$ns attach-agent $n0 $tcp0

set sink0 [new Agent/TCPSink]
$ns attach-agent $n2 $sink0

$ns connect $tcp0 $sink0
$tcp0 set fid_ 1


# file transfer protocol 0

set ftp0 [new Application/FTP]
$ftp0 attach-agent $tcp0
$ftp0 set type_ FTP


#tcp 1
set tcp1 [new Agent/TCP]
$tcp1 set class_ 2

$ns attach-agent $n1 $tcp1

set sink1 [new Agent/TCPSink]
$ns attach-agent $n3 $sink1

$ns connect $tcp1 $sink1
$tcp1 set fid_ 2


# file transfer protocol 1

set ftp1 [new Application/FTP]
$ftp1 attach-agent $tcp1
$ftp1 set type_ FTP

# simulating
$ns at 0.1 "$ftp0 start"
$ns at 0.1 "$ftp1 start"
$ns at 5.0 "$ftp0 stop"
$ns at 5.0 "$ftp1 stop"

$ns at 5.2 "finish"

$ns run
