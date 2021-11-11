FROM node:8.9.3

ENV APP_DIR /home/app
ENV PORT 5000

# extract bundle
RUN mkdir ${APP_DIR}
WORKDIR ${APP_DIR}
ADD . .

# install meteor dependencies
RUN npm install --unsafe-perm
RUN npm run compile

# install runtime dependencies
RUN npm install -g forever

CMD forever --minUptime 1000 --spinSleepTime 1000 ${APP_DIR}/dist/start.js

EXPOSE 5000