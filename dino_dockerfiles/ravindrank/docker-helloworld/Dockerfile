FROM ubuntu:latest
MAINTAINER Ravindran Keshavan "ravindran.k@gmail.com"

RUN apt-get update
RUN apt-get install apt-utils wget -y
RUN apt-get install libunwind8 libicu55 libcurl3 -y
RUN wget https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-alpha.11/powershell_6.0.0-alpha.11-1ubuntu1.16.04.1_amd64.deb
RUN dpkg -i powershell_6.0.0-alpha.11-1ubuntu1.16.04.1_amd64.deb
RUN powershell

