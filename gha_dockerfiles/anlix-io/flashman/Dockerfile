FROM node:12

# APP information
MAINTAINER anlix "guisenges@gmail.com"

ENV FLM_MQTTS_DOMAIN ""
ENV FLM_ACME_FILE ""
ENV FLM_KEY_MQTT_FILE ""
ENV FLM_CERT_MQTT_FILE ""
ENV FLM_IMG_RELEASE_DIR "./public/firmwares/"
ENV FLM_ALLOW_DEV_UPDATE_REST_DATA false
ENV FLM_MONGODB_HOST "localhost"
ENV FLM_ADM_USER "admin"
ENV FLM_ADM_PASS "flashman"
ENV FLM_CONCURRENT_UPDATES_LIMIT 5
ENV FLM_WEB_PORT "8000"
ENV FLM_GENIE_IGNORED true

WORKDIR /app

COPY /app.js /mqtts.js /sio.js /LICENSE /package.json /docker/environment.config.json /docker/wait-for-it.sh /app/
COPY /bin /app/bin
COPY /controllers /app/controllers
COPY /models /app/models
COPY /public /app/public
COPY /routes /app/routes
COPY /views /app/views

# Run as root
RUN mkdir -p /app/public/firmwares \
	&& chown -R node:node /app /app/public/firmwares
RUN npm install pm2 -g

# Run as user node
USER node
RUN npm install --production

EXPOSE 8000
EXPOSE 1883
EXPOSE 8883

CMD bash /app/wait-for-it.sh ${FLM_MONGODB_HOST}:27017 -t 0 -- pm2-docker start environment.config.json
