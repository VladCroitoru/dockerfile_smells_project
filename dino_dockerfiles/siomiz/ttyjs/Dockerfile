FROM node:0.10

MAINTAINER Tomohisa Kusano <siomiz@gmail.com>

RUN npm install tty.js -g \
	&& npm cache clean

RUN useradd -d /home/user user \
	&& mkdir -p /home/user/.tty.js \
	&& chown -R user.user /home/user

ADD cmd.js /cmd.js

USER user

WORKDIR /home/user

CMD ["/usr/local/bin/node", "/cmd.js"]

EXPOSE 8080
