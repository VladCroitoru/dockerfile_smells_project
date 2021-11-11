FROM ubuntu:15.04
MAINTAINER nahidul kibria <nahidupa@gmail.com>
# Install packages  
RUN apt-get update \
 && apt-get install -y openjdk-7-jdk gcc-multilib

# Create workspace
RUN mkdir /work

VOLUME /work

WORKDIR /work

COPY ./apktool /work
COPY ./apktool.jar /work

# Move bins to /usr/local/bin
RUN mv apktool.jar apktool /usr/local/bin

# Allow execution
RUN chmod +x /usr/local/bin/apktool.jar /usr/local/bin/apktool


# Clean up 
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /work/* 

ENTRYPOINT ["apktool"]
