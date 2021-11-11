FROM ubuntu:latest
MAINTAINER Matt Koski <maccam912@gmail.com>

RUN apt-get upgrade && apt-get update -y
RUN apt-get install git python build-essential wget screen tmux curl vim -y

RUN mkdir /Development
RUN cd /Development && git clone git://github.com/joyent/node

RUN cd /Development/node && ./configure && make && make install
RUN rm -rf /Development/node

RUN npm install -g meteorite bower grunt-cli yo demeteorizer

#RUN curl https://j.mp/spf13-vim3 -L > spf13-vim.sh && sh spf13-vim.sh

EXPOSE 80:80
EXPOSE 443:443
EXPOSE 3000:3000

RUN cd /Development && wget -O - https://install.meteor.com/ | sh

#RUN cp ~/.meteor/tools/latest/launch-meteor /usr/bin/meteor

RUN echo "Done. Run 'mrt create <app-name>' to create meteor app. cd into the folder created and run 'meteor' to run your webapp locally."
