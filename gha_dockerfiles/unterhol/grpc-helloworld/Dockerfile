FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install wget -y

RUN wget https://github.com/fullstorydev/grpcurl/releases/download/v1.8.2/grpcurl_1.8.2_linux_x86_64.tar.gz

RUN tar -xvzf grpcurl_1.8.2_linux_x86_64.tar.gz
RUN chmod +x grpcurl
RUN mv grpcurl /usr/local/bin/grpcurl
RUN grpcurl --help