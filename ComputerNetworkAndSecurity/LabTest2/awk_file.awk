BEGIN {
number_of_drops=0;
number_of_received=0;
number_of_enqued=0;
number_of_dequeue=0;
}
{
parameter1=$1
paramter2=$2
parameter3=$3
parameter4=$4
parameter5=$5
parameter6=$6

parameter8=$8
parameter9=$9
parameter10=$10
parameter11=$11
parameter12=$12
if (parameter1=="r" && parameter3="4" && parameter4="2")
number_of_received++;

if(parameter1=="d"  &&  parameter3="4" && parameter4="3")
number_of_drops++;

}
END {
printf("number of received:%d",number_of_received);
printf("\nnumber of drops:%d",number_of_drops);
}