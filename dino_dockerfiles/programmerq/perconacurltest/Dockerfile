FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install curl
RUN curl -vI https://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm
RUN apt-get -y install wget
RUN wget https://www.percona.com/downloads/percona-release/percona-release-0.0-1.x86_64.rpm
RUN apt-get -y install traceroute
RUN traceroute www.percona.com
RUN ping -c 1 www.percona.com
