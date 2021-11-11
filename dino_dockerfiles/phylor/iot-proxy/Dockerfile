FROM node

RUN mkdir /opt/iot-proxy
COPY . /opt/iot-proxy

WORKDIR /opt/iot-proxy
RUN npm install

CMD [ "node", "index.js" ]
