FROM       ubuntu
MAINTAINER Briehan Lombaard
RUN        echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN        apt-get update
RUN        apt-get upgrade -y
RUN        apt-get install -y bitcoind
EXPOSE     8333
ENTRYPOINT ["bitcoind"]
CMD        ["--help"]
