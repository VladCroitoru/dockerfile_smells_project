FROM ubuntu:latest

MAINTAINER SeveirRoy

RUN apt-get update && \
    apt-get install wget gcc libc6-dev -y --no-install-recommends && \
    cd /home && \  
    wget https://raw.githubusercontent.com/SeveirRoy/cpuIntensiveAPP/master/cpuIntensiveApp.c --no-check-certificate && \
    gcc cpuIntensiveApp.c -o cpuIntensiveApp

CMD ["/home/cpuIntensiveApp"]
