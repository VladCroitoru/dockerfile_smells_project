FROM node:6-wheezy

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install	&& bower install --allow-root

RUN groupadd -r ah && useradd -mr -g ah ah
USER ah

EXPOSE 6000
ENTRYPOINT /app/docker-entrypoint.sh 6000

