FROM node:10-alpine

ARG API_URL
ARG ELICIT_LANDING_URL
ARG API_SCHEME

RUN apk add git

RUN npm uninstall gulp -g

RUN mkdir /experiment-frontend

WORKDIR /experiment-frontend

COPY ./package.json /experiment-frontend/
# COPY ./package-lock.json /experiment-frontend/

RUN ls -als

RUN npm install

RUN npm install -g gulp

COPY . /experiment-frontend

RUN sed -i'' -E "s/(\s+portalPath\: ).*/\1\"$API_SCHEME:\/\/$API_URL\",/g" gulpfile.js
RUN sed -i'' -E "s/(\s+elicitLandingPath\: ).*/\1\"$API_SCHEME:\/\/$ELICIT_LANDING_URL\",/g" gulpfile.js

RUN cat gulpfile.js | grep portalPath

RUN npm --version

RUN node --version

RUN gulp  --version

RUN gulp build

CMD ["/bin/sh", "./run.sh"]
