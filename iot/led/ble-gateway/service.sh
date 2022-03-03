#!/bin/sh
set -e
SCRIPT_DIR=$( cd "$( dirname "$0" )" >/dev/null 2>&1 && pwd )

cd "$SCRIPT_DIR"
sudo python3 ./gateway.py "$@" > /home/pi/pi-gateway/gateway.log 2>&1