# This installs the latest development build of vision.ai's VMX server
# visit us on github, docker hub, and on the web at https://vision.ai
# 
# This is an experimental "concatenation" of the individual vision.ai
# containers we typically use.


FROM ubuntu
MAINTAINER Tom Malisiewicz tom@vision.ai

#Setup vmx-environment
RUN apt-get update && apt-get -y install libgmp10 libxt6 libxext6 libxmu6

#start mcr
RUN \
  apt-get update && apt-get install -y wget tar unzip

###INSTALL MATLAB Runtime
RUN mkdir -p /root/matlab_installer
ADD matlab_options.txt /root/matlab_installer/matlab_options.txt

WORKDIR /root/matlab_installer
RUN wget -nc http://www.mathworks.com/supportfiles/downloads/R2014a/deployment_files/R2014a/installers/glnxa64/MCR_R2014a_glnxa64_installer.zip && \
    unzip MCR_R2014a_glnxa64_installer.zip && \
    ./install -inputFile matlab_options.txt && \
    rm -rf /root/matlab_installer
#VOLUME /root/MATLAB

#################  vmx middle

RUN mkdir -p /vmx/middle
WORKDIR /vmx

RUN \ 
  wget -q http://files.vision.ai/vmx/VMXmiddle/Linux/VMXmiddle_Linux.latest.tar.gz && \
  cd middle && \                                                         
  gzip -d ../VMXmiddle_Linux.latest.tar.gz && \
  tar xf ../VMXmiddle_Linux.latest.tar && \
  rm ../VMXmiddle_Linux.latest.tar && \
  echo "Version is " `cat version`

#VOLUME /vmx/middle

###################### vmx-server

RUN mkdir -p /vmx/build
#VOLUME /vmx/build

WORKDIR /vmx

RUN \
  wget -q http://files.vision.ai/vmx/VMXserver/Linux/VMXserver_Linux.latest.tar.gz && \
  gzip -d VMXserver_Linux.latest.tar.gz && \
  tar xf VMXserver_Linux.latest.tar && \
  rm VMXserver_Linux.latest.tar && \
  echo "Version is " `cat build/version` && \
  mkdir -p /vmx/data && \
  cd /vmx/data && \
  wget -q http://files.vision.ai/vmx/pretrained/3f61ce5c7642bc2f24f7286f600b3e6b && \
  wget -q http://files.vision.ai/vmx/pretrained/109e8c80074201cda9cfe4d167868337      

ADD config.json /vmx/build/config.json
#VOLUME /vmx/data

#####################   appbuilder
RUN mkdir -p /vmx/middle
WORKDIR /vmx/middle
RUN \
  wget -q http://files.vision.ai/vmx/vmxAppBuilder/vmxAppBuilder.latest.tar.gz &&\ 
  gzip -d vmxAppBuilder.latest.tar.gz &&\
  tar xf vmxAppBuilder.latest.tar &&\ 
  rm vmxAppBuilder.latest.tar &&\
  wget -q http://files.vision.ai/vmx/VMXdocs/VMXdocs.latest.tar.gz &&\
  gzip -d VMXdocs.latest.tar.gz &&\
  tar xf VMXdocs.latest.tar -C static &&\
  rm VMXdocs.latest.tar
#VOLUME /vmx/middle/static

######################  user data
RUN mkdir -p /vmx/models

VOLUME /vmx/models

#Exposing this volume breaks the Kinematic install
#VOLUME /vmx/sessions

EXPOSE 3000
CMD ["/vmx/middle/vmx"]
