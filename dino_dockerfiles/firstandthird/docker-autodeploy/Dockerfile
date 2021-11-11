FROM firstandthird/node:8.9-2-onbuild

RUN apk add --update docker

RUN ./bin/install-docker-app

ENV CONFIG_PATH /config
ENV NODE_ENV production

CMD ["rapptor"]
