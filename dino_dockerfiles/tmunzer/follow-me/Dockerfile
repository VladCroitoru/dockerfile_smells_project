FROM node:6-wheezy
LABEL fr.ah-lab.followme.version="0.0.3"
LABEL fr.ah-lab.followme.release-date="2018-01-01"

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install	&& bower install --allow-root

RUN groupadd -r ah && useradd -mr -g ah ah
USER ah

EXPOSE 51801
ENTRYPOINT /app/docker-entrypoint.sh 51801

