FROM node:8.0.0-alpine
LABEL maintainer "andrey@subbotin.me"

CMD ["sh"]

ENV NODE_ENV development
ENV NPM_CONFIG_LOGLEVEL error
RUN npm install -g --non-interactive yarn@0.24.6

RUN mkdir -p /app
WORKDIR /app
