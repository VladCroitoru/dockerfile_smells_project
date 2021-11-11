FROM mhart/alpine-node:7.5.0

MAINTAINER steve@grosbois.fr

# Timezone
ENV TIMEZONE Europe/Paris

RUN	apk add --update tzdata && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone

RUN	apk del tzdata && \
    rm -rf /var/cache/apk/*

RUN addgroup -S nodejs && adduser -S -g nodejs nodejs

USER nodejs

# Create app directory
RUN mkdir -p /home/nodejs/app
WORKDIR /home/nodejs/app

CMD [ "node", "." ]

# Install app dependencies
COPY package.json /home/nodejs/app/
RUN npm install

# Bundle app source
COPY . /home/nodejs/app
