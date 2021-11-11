FROM debian:jessie

MAINTAINER Olivier Girardot <o.girardot@lateral-thoughts.com>

RUN apt-get update
RUN apt-get install -y wget default-jdk
RUN wget -q http://d3kbcqa49mib13.cloudfront.net/spark-1.4.0-bin-hadoop2.6.tgz
RUN tar -zxvf spark-1.4.0-bin-hadoop2.6.tgz
RUN rm spark-1.4.0-bin-hadoop2.6.tgz
RUN mv spark-1.4.0-bin-hadoop2.6 /usr/local/spark/

CMD ["/usr/local/spark/bin/spark-shell"]
