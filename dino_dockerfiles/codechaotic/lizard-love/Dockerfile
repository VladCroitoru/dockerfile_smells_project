# Koa2 requires Node 7.x
# Node likes to ignore the default SIGTERM signal sent by docker-compose. To fix this
# I use dumb-init as the PID 1 [See https://github.com/Yelp/dumb-init]

FROM node:7-slim
WORKDIR /app
ADD . /app

RUN apt-get update \
  && wget https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64.deb \
  && dpkg -i dumb-init_*.deb \
  && rm dumb-init_*.deb \
  && npm install --production

ENTRYPOINT ["dumb-init"]
CMD ["npm", "-q", "start"]
STOPSIGNAL SIGTERM
EXPOSE 3000
