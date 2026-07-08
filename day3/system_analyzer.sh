info_count=0
error_count=0
warn_count=0

#function to analyze log line
analyze_log(){
line=$1
if echo "$line"| grep -q "INFO"
then
((info_count++))
elif echo "$line" | grep -q "WARNING"
then
((warn_count++))
else
((error_count++))
fi
}
#function to determine the system status
check_status(){
if [[ $error_count -gt 10 ]]
then 
     status="Critical"
elif [[ $error_count -gt 0 ]]
then 
    status="warning"
else
   status="Healthy"
fi
}
 
#read input file
echo "Enter log file: "
read logfile
if [[ ! -f $logfile ]]
then
   echo "Files no exist"
   exit
fi

#loop through the file
while read line
do
analyze_log "$line" 
done < $logfile

#determine status
check_status
#generate the report
{
echo "System Log Analyzer Report"
echo "============================"
echo "INFO Count: $info_count"
echo "WARNING Count: $warn_count"
echo "ERROR Count: $error_count"
echo
echo "System status: $status"
} > report.txt
echo "Report Generated: report.txt"
