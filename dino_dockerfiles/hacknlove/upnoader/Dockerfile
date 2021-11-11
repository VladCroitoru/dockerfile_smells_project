FROM node:onbuild
MAINTAINER hacknlove

VOLUME /uploads

WORKDIR /upnoader

ADD package.json /upnoader
RUN npm install

COPY index.js /upnoader
COPY start.sh /upnoader

CMD /upnoader/start.sh
