FROM ubuntu
MAINTAINER mwaeckerlin
ENV TERM "xterm"

ENV USER ""

EXPOSE 80

RUN apt-get update
RUN apt-get install -y phpldapadmin

ADD start.sh /start.sh
CMD /start.sh
