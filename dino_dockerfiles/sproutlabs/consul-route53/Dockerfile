FROM consul:latest

RUN apk add --no-cache py-pip ca-certificates wget nodejs
RUN mkdir -p /src
WORKDIR /src

COPY package.json /src/
RUN npm install

COPY . /src

ENTRYPOINT ["/src/start.sh"]
