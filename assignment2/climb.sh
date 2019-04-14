#!/bin/bash

function climb(){
  # variable used to count down
  declare -i count

# if no argument is given just go down one directory
  if [ $# -eq 0 ]; then
    cd */  # this make it go down the directory
  else
    count=$1
    while [ "$count" != 0 ]; do
      cd */
      count=$count-1
    done
  fi
}
