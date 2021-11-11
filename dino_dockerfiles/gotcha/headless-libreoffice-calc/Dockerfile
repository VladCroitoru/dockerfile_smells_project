FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y -q --no-install-recommends install software-properties-common=0.96.20.7
RUN add-apt-repository ppa:libreoffice/ppa
RUN apt-get update
RUN apt-get -y -q --no-install-recommends install libreoffice-calc=1:6.0.1~rc1-0ubuntu0.16.04.1~lo1
RUN apt-get -y -q --no-install-recommends install python3-uno=1:6.0.1~rc1-0ubuntu0.16.04.1~lo1
# setuptools is needed to install pyoo
RUN apt-get -y -q --no-install-recommends install python3-setuptools=20.7.0-1
RUN apt-get -y -q --no-install-recommends install python3-pip=8.1.1-2ubuntu0.4
RUN pip3 install pip==9.0.1
RUN pip3 install pyoo==1.3
