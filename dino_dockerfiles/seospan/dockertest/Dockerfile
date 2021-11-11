FROM ubuntu:16.04
MAINTAINER  Seospan
RUN locale-gen fr_FR.UTF-8
ENV LANG fr_FR.UTF-8 
ENV LANGUAGE fr_FR.UTF-8 
ENV LC_ALL fr_FR.UTF-8  
RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade
VOLUME /home/data_c
CMD ["/bin/bash"]
