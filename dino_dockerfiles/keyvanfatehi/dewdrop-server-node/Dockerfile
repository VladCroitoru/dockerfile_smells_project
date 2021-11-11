FROM dockerfile/nodejs
MAINTAINER Keyvan Fatehi <keyvanfatehi@gmail.com>
RUN mkdir /dewdrop
ADD package.json /dewdrop/package.json
RUN cd /dewdrop && npm install
ADD src /dewdrop/src
ADD server.js /dewdrop/server.js
ENV DEWDROP_STORAGE /data
EXPOSE 3000
ENTRYPOINT ["node", "/dewdrop/server.js"]
