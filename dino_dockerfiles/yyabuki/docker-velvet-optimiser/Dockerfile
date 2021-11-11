FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
# a bit modified Michael Barton's Dockerfile, Procfile and run files.

RUN apt-get update -y
RUN apt-get install -y velvet bsdmainutils bioperl procps

ADD http://www.vicbioinformatics.com/VelvetOptimiser-2.2.5.tar.gz /tmp/
RUN tar xzf /tmp/VelvetOptimiser-2.2.5.tar.gz
RUN mv /VelvetOptimiser-2.2.5 /usr/local/velvet_optimiser
ENV PATH $PATH:/usr/local/velvet_optimiser

ADD run /usr/local/bin/
ADD Procfile /

ENTRYPOINT ["/usr/local/bin/run"]
