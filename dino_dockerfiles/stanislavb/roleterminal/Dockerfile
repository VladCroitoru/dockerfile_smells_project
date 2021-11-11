FROM node:7.1.0
EXPOSE 8888
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

CMD [ "./node_modules/roleHaven/docker-start.sh" ]
