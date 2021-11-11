FROM node:6.10-alpine

ENV TAMARIN_VERSION 0.0.8

RUN npm install -g strongloop

RUN apk add --no-cache ca-certificates openssl

RUN wget -O tamarin.tar.gz https://github.com/tuyakhov/tamarin/archive/v${TAMARIN_VERSION}.tar.gz \
    && tar -xvzf "tamarin.tar.gz" \
    && rm tamarin.tar.gz

WORKDIR /tamarin-${TAMARIN_VERSION}

RUN npm install --production \
    && npm cache clean \
    && rm -rf /tmp/npm*

CMD ["npm", "start"]

EXPOSE 3000 51459
