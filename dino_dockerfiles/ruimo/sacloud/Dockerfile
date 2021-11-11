FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get -y install nodejs npm git
RUN npm install -g sacloud
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN sacloud --install >> ~/.bashrc
RUN mkdir ~/.node-completion
ADD zone1.sh /usr/bin/zone1.sh
ADD zone2.sh /usr/bin/zone2.sh
ADD setToken.sh /usr/bin/setToken.sh

CMD ["/bin/bash"]

