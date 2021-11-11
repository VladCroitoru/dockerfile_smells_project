FROM node:lts
MAINTAINER Michael J. Stealey

VOLUME /code
WORKDIR /code

COPY ./package.json ./
COPY ./package-lock.json ./
COPY ./src ./src
COPY ./public ./public
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

WORKDIR /

EXPOSE 3000 5000

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["run_server"]

