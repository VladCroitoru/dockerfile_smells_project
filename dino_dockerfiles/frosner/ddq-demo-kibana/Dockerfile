FROM phusion/baseimage:0.9.18

MAINTAINER Frank Rosner <frank@fam-rosner.de>

RUN curl -s https://download.elastic.co/kibana/kibana/kibana-4.5.0-linux-x64.tar.gz | tar -xz -C /usr/local \
  && mv /usr/local/kibana-4.5.0-linux-x64 /usr/local/kibana

ADD kibana.yml /usr/local/kibana/config/kibana.yml

RUN mkdir /etc/service/kibana
ADD start-kibana.sh /etc/service/kibana/run
RUN chmod a+x /etc/service/kibana/run

CMD ["/sbin/my_init"]
