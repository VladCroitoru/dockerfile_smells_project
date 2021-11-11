FROM node:4

MAINTAINER Minh-Quan TRAN "account@itscaro.me"

RUN npm install -g npm

COPY src/config.dist.json /app/src/config.json

COPY package.json /app/package.json
RUN cd /app && npm install --production

COPY start.sh /start.sh
COPY . /app

EXPOSE 8099
ENV HOST=127.0.0.1 \
	PORT=8099 \
	CALIBRE_PATH=""
	
ENTRYPOINT [ "/start.sh"]
