# michaloo/punch
#
# VERSION               0.0.1

FROM ubuntu:14.04


# install usefull tools
RUN apt-get update -y && \
    apt-get install -y supervisor curl git

# install nodejs
RUN echo 'deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu precise main' > /etc/apt/sources.list.d/nodejs.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12 && \
    apt-get update -y && \
    apt-get install nodejs -y


# install webdev tools and punch!
RUN npm install -g grunt-cli bower gulp punch

EXPOSE 80

CMD ["/bin/bash"]
