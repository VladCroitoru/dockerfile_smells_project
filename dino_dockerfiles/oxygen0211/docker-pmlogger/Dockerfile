FROM ubuntu:trusty
MAINTAINER jengelhardt211@gmail.com

ADD start-pmlogger.sh /usr/local/bin/start-pmlogger.sh

RUN apt-get update &&\
    apt-get install -y pcp &&\
    chmod 755 /usr/local/bin/start-pmlogger.sh


ENTRYPOINT  ["/usr/local/bin/start-pmlogger.sh"]
CMD ["localhost", "localhost"]
