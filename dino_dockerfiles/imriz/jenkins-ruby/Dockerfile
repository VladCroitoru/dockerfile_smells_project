FROM ruby
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>/etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends git
RUN git config --global http.sslVerify false
RUN apt-get install -y --no-install-recommends  -t jessie-backports openjdk-8-jdk

