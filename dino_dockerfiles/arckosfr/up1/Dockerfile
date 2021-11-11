FROM xataz/node:latest-onbuild
RUN apk --update add bash wget git unzip ca-certificates && \
        cd / && git clone https://github.com/Upload/Up1 && \
		cd /Up1/server && \
    apk del wget unzip git && rm -rf /var/cache/apk/* && \
    npm install

ADD start.sh /start.sh

EXPOSE 80 443

WORKDIR /Up1/server

ENV NODE_ENV production

CMD ["bash","/start.sh"]
