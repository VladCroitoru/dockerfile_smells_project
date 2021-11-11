FROM node:9

WORKDIR /src

COPY . /src

RUN npm install && npm link

ENTRYPOINT ["dlt"]
