FROM java:8-jdk
MAINTAINER Ruben Malchow <ruben.malchow@mcon-group.com>
RUN apt-get update -y && apt-get install -y netcat && apt-get clean all -y
COPY assets/* /assets/
