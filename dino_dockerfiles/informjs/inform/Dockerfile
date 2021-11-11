FROM alpine
MAINTAINER Bailey Stoner <code@monokro.me>


RUN apk update
RUN apk add build-base
RUN apk add nodejs
RUN apk add python
RUN apk add zeromq libzmq zeromq-dev


RUN ldconfig /


RUN npm install -g coffee-script


ADD shared /opt/informjs/shared
WORKDIR /opt/informjs/shared
RUN rm -rf node_modules
RUN npm install
RUN npm link
RUN make


ADD plugins /opt/informjs/plugins


WORKDIR /opt/informjs/plugins/tropo-sms
RUN rm -rf node_modules
RUN npm install
RUN npm link
RUN npm link inform-shared


WORKDIR /opt/informjs/plugins/tropo-sms
RUN rm -rf node_modules
RUN npm install
RUN npm link


ADD daemon /opt/informjs/daemon
WORKDIR /opt/informjs/daemon
RUN rm -rf node_modules
RUN npm install
RUN npm link
RUN npm link inform-shared
RUN npm link inform-daemon


ADD etc/informd.example.yml /etc/informd.yml


EXPOSE 5000


CMD ["bin/informd"]
