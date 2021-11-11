FROM node:5.8

EXPOSE 8061

ADD . /iframely

WORKDIR /iframely

RUN apt-get update && \
	apt-get install libkrb5-dev && \
	apt-get clean

RUN npm config set color false
RUN npm config set loglevel warn
RUN npm config set progress false

RUN npm install

CMD ["node", "server"]
