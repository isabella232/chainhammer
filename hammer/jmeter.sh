#!/bin/bash
../../jmeter/apache-jmeter-5.2.1/bin/./jmeter -n -t deploy.jmx \
    -Jurl=54.165.168.127   -Jport=22000 -Jaccount=0x31b579ae36d2e177808422c89fa4c4491a6b71a2 \
    -Jthread=5 -Jloop=100 -Jjmeter.save.saveservice.output_format=xml \
    -Jjmeter.save.saveservice.response_data=true -Jjmeter.save.saveservice.samplerData=true  \
    -Jjmeter.save.saveservice.requestHeaders=true -Jjmeter.save.saveservice.url=true     \
