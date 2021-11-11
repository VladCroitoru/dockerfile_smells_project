FROM debian:wheezy
MAINTAINER jj
ENV DEBIAN_FRONTEND noninteractive
RUN  apt-get update && apt-get -y install python-flask unzip && rm -rf /var/lib/{apt,dpkg,cache,log}
ADD https://github.com/httpPrincess/fakedEpicServer/archive/master.zip /app/
RUN cd /app/ && unzip master.zip && rm master.zip 
EXPOSE 5000 
WORKDIR /app/fakedEpicServer-master/
CMD python simpleEpic.py
