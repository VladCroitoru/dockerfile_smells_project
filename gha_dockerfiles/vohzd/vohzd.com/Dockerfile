FROM node:14.15.3

ARG EMAIL_SERVER_ENDPOINT=${EMAIL_SERVER_ENDPOINT}
ARG EMAIL_PASSWORD=${EMAIL_PASSWORD}

RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app
COPY . /usr/src/nuxt-app/

RUN npm install
RUN npm run build

EXPOSE 80

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=80

CMD [ "npm", "run", "start" ]
