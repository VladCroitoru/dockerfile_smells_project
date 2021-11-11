FROM debian:latest
MAINTAINER Matt Bailey <m@mdb.io>

# To get rid of error messages like "debconf: unable to initialize frontend: Dialog":
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN echo "deb http://ppa.launchpad.net/jcfp/ppa/ubuntu precise main" | tee -a /etc/apt/sources.list
RUN echo "deb http://http.debian.net/debian wheezy non-free" | tee -a /etc/apt/sources.list

RUN apt-get -q update && \
    apt-get install -qy --force-yes sabnzbdplus \
    par2 python-yenc unzip unrar

# apt clean
RUN apt-get clean &&\
  rm -rf /var/lib/apt/lists/* &&\
  rm -rf /tmp/*

VOLUME /config
VOLUME /data

ADD ./start.sh /start.sh
RUN chmod u+x  /start.sh

EXPOSE 8080 9090

CMD ["/start.sh"]
