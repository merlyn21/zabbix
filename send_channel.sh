#!/bin/bash

mess="$1
$2"

python3 /usr/lib/zabbix/alertscripts/to_channel_z.py "$mess"
