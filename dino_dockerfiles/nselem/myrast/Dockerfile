FROM ubuntu:14.04
Maintainer nselem35

RUN apt-get -qq update

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install blast2 
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install libwxgtk2.8-0 
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install libdb4.8
RUN DEBIAN_FRONTEND=noninteractive apt-get -qqy install libxml2

RUN apt-get install -y curl
RUN apt-get install -y build-essential
RUN apt-get install -y wget

#RUN curl -L http://blog.theseed.org/downloads/sas.tgz > sas.tgz
RUN mkdir /opt/sas && wget http://blog.theseed.org/downloads/sas.tgz 
RUN tar -xvzf sas.tgz -C /opt/sas
RUN cd /opt/sas/modules && ./BUILD_MODULES

RUN chmod -R 777 /opt
RUN apt-get install -y git
RUN git clone https://github.com/nselem/myrast.git  /opt/myrast
RUN chmod -R 777 /opt/myrast

ENV PATH /opt/sas/bin:$PATH:/opt/myrast
ENV PERL5LIB $PERL5LIB:/opt/sas/lib:/opt/sas/modules/lib
WORKDIR /home
