#
# development tools for Google apps script.
#
FROM ubuntu:14.04
MAINTAINER tyskdm <tsuyoshi.kodama@gmail.com>
RUN apt-get update
#
# locale setting
#
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
#
# Java
#
RUN apt-get install -y openjdk-7-jdk
#
# Apach ant
#
RUN apt-get install -y ant
#
# Google closure compiler
# https://developers.google.com/closure/compiler/
#
RUN mkdir /usr/local/closure-compiler
ADD http://dl.google.com/closure-compiler/compiler-latest.tar.gz /usr/local/closure-compiler/compiler-latest.tar.gz
RUN tar xvfz /usr/local/closure-compiler/compiler-latest.tar.gz -C /usr/local/closure-compiler
RUN chmod 644 /usr/local/closure-compiler/compiler.jar
#
# Google closure linter
# https://developers.google.com/closure/utilities/docs/linter_howto
#
RUN apt-get install -y python-pip
RUN apt-get install -y subversion
RUN pip install https://closure-linter.googlecode.com/svn/trunk/
#
# nodejs
#
RUN apt-get install -y nodejs npm
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10
#
# gas-manager
#
RUN npm install -g gas-manager
