FROM errordeveloper/iojs-minimal-runtime:v1.0.1
MAINTAINER Christian Beedgen <raychaser@gmail.com>
ADD . /srv/app
WORKDIR /srv/app
RUN npm install
EXPOSE 80
ENTRYPOINT ["node", "index.js"]