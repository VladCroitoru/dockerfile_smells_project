FROM node:6-wheezy
LABEL fr.ah-lab.analytics.version="0.0.3"
LABEL fr.ah-lab.analytics.release-date="2017-03-11"

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install	&& bower install --allow-root

RUN groupadd -r ah && useradd -mr -g ah ah
USER ah

EXPOSE 51362
ENTRYPOINT /app/docker-entrypoint.sh 51362

