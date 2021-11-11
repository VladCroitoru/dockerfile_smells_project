FROM healthcatalyst/fabric.baseos:latest

LABEL maintainer="Health Catalyst"
LABEL version="1.0"

RUN yum -y update

RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \
	&& yum -y install nodejs

ADD docker-entrypoint.sh ./docker-entrypoint.sh

RUN dos2unix ./docker-entrypoint.sh \
	&& chmod +x ./docker-entrypoint.sh

RUN mkdir -p /app && mkdir -p /app/public

ADD package.json /app/package.json
ADD mini-webserver.js /app/mini-webserver.js

RUN cd /app && npm install

VOLUME ["/app/public"]

EXPOSE 3000

CMD ["node", "/app/mini-webserver.js"]

ENTRYPOINT [ "./docker-entrypoint.sh" ]