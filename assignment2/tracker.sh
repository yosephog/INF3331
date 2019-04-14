
# the program can be runned by giving the argument start task_name
# for example ./tracker.sh start reading_1

# when the first argumnet is  start it will start the time
if [ "$1" == "start" ]; then
  startTime=$(date)
  input=$1
  # while the input stop is not given it will simple wait
  while [ "$input" != "stop" ]; do
    #Enter stop to end the timing or task to view the the current task
    read -rp "Enter stop/task --:" "input"
    if [ "$input" == "task" ]; then
      echo "current task is -: $2"
    fi
  done
  endTime=$(date)
fi

# pipping it to a textfile
echo "start -: $startTime
task -: $2
end -: $endTime

              " >> log.txt

export LOGFILE=log.txt
