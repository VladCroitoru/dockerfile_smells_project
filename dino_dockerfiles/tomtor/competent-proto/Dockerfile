FROM ubuntu:16.04
RUN apt-get -y update && apt-get install -y ssh netcat-openbsd python3 ftp
RUN mkdir /competent
RUN ssh-keygen -t rsa -N "" -f /competent/competent.key
COPY competent.sh /competent
CMD sh /competent/competent.sh
