
# starts the same way as the tracker.sh

if [ "$1" == "start" ]; then
  startTime=$(date +%H%M%S) # used to format it so i can be able to substract
  input=read
  while [ "$input" != "stop" ]; do
    read -rp "Enter stop/task" "input"
    if [ "$input" == "task" ]; then
      echo "current task is -: $2"
    fi
  done
  endTime=$(date +%H%M%S)
  diff=$(($endTime - $startTime))
  echo "$2 -: $diff
                " >> time_log.txt

  export LOGFILE=time_log.txt
fi
