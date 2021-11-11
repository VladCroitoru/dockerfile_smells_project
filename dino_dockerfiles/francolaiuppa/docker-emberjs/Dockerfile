FROM francolaiuppa/docker-bower-gulp
MAINTAINER francolaiuppa
RUN ["npm","install","-g","ember-cli"]
VOLUME /usr/src/app
WORKDIR /usr/src/app
EXPOSE 4200
EXPOSE 49152
CMD ["ember","server"]
