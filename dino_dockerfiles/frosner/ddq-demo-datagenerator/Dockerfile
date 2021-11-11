FROM phusion/baseimage:0.9.18

MAINTAINER Frank Rosner <frank@fam-rosner.de>

RUN mkdir /etc/service/datagenerator
ADD datagenerator.sh /etc/service/datagenerator/run
RUN chmod a+x /etc/service/datagenerator/run

CMD ["/sbin/my_init"]
