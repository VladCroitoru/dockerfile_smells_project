FROM node:7-alpine

ENV PSITRANSFER_UPLOAD_DIR=/data \
    NODE_ENV=production

MAINTAINER k0nsl <git@k0nsl.org>

WORKDIR /app

ADD *.js package.json README.md /app/
ADD lib /app/lib
ADD app /app/app
ADD public /app/public

RUN apk --update add nano && apk upgrade

# Rebuild the frontend apps
RUN cd app && \
    NODE_ENV=dev npm install --quiet 1>/dev/null && \
    npm run build && \
    cd .. && rm -rf app

# Add user
RUN adduser -D -s /sbin/nologin transfer01

# Install backend dependencies
RUN mkdir /data && \
    chown transfer01 /data && \
    npm install --quiet 1>/dev/null

EXPOSE 3000
VOLUME ["/data"]

USER transfer01

HEALTHCHECK CMD wget -O /dev/null -q http://localhost:3000

CMD ["node", "app.js"]
