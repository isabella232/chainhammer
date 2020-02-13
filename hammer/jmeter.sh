#!/bin/bash
apache-jmeter-5.2.1/bin/./jmeter -n -t deploy.jmx \
    -Jurl=$1   -Jport=22000 -Jaccount=$2 \
    -Jthread=1 -Jloop=10000 -Jjmeter.save.saveservice.output_format=xml \
    -Jjmeter.save.saveservice.response_data=true -Jjmeter.save.saveservice.samplerData=true  \
    -Jjmeter.save.saveservice.requestHeaders=true -Jjmeter.save.saveservice.url=true     
