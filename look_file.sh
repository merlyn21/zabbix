#!/bin/bash

#look_file.sh -size  возвращает размер файла
#look_file.sh -time  возвращает возраст файла в часах

#+%Y%m%d%H%M%S

path="/path_to_look_file"
diff_hour=25

name_f=$(ls -t $path | head -n 1)
#echo $name_f

date_create=$(date -r $path/$file +%s)
#echo $date_create
date_now=$(date +%s)
#echo $date_now
let date_diff=($date_now-$date_create)/3600
if [ $1 == '-time' ]; then
  echo $date_diff
fi
if [ $1 == '-size' ]; then
  size=$(du -b $path/$name_f | awk '{print $1}')
  echo $size
fi
