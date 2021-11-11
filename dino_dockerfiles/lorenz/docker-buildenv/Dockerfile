FROM ubuntu:14.04
RUN sed -i 's|http://archive.ubuntu.com/ubuntu/|mirror://mirrors.ubuntu.com/mirrors.txt|g' /etc/apt/sources.list
RUN apt-get update && apt-get install -yy nodejs nodejs-legacy npm git docker.io #17072015
RUN npm update -g npm
RUN npm install -g bower gulp
CMD ["/bin/bash"]