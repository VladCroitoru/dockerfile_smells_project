FROM node:6-wheezy

RUN npm install -g bower

COPY ./src /app/

WORKDIR /app

RUN npm	install

RUN groupadd -r ah && useradd -mr -g ah ah
USER ah

EXPOSE 51366
ENTRYPOINT /app/docker-entrypoint.sh 51366
