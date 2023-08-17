#!/bin/bash
for i in `seq 1 64`; do
  ../utils/distributed_computing/start_computing_client.py -p 2050 > /dev/null 2>&1 &
done 

