FROM golang
MAINTAINER Chanchai Junlouchai (neverlock.org) "neverlock@gmail.com"

RUN apt-get update && apt-get install -y git 

WORKDIR /go/src

RUN git clone https://github.com/neverlock/PacktpubFreeAlert.git

WORKDIR /go/src/PacktpubFreeAlert
RUN git checkout 7580aa14153b9b96dcf48adcad4ec4af4f6336c8

ADD init.sh /init.sh
RUN chmod +x /init.sh


CMD ["/init.sh"]
