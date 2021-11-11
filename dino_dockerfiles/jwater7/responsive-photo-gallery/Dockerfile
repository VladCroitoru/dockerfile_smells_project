FROM node:lts-alpine
LABEL maintainer "j"

# Backend node_modules
WORKDIR /usr/src/app

# Add ffmpeg runtime dependency
RUN apk add --no-cache ffmpeg

# Add sharp library dependencies, see: http://sharp.dimens.io/en/stable/install/
RUN apk add vips-dev fftw-dev build-base --update-cache \
    --repository https://alpine.global.ssl.fastly.net/alpine/edge/community/ \
    --repository https://alpine.global.ssl.fastly.net/alpine/edge/main \
    && rm -rf /var/cache/apk/*

# Install dependencies
COPY package.json ./

#RUN npm install
# Build using gyp dependencies for sharp, see https://github.com/nodejs/docker-node/issues/282
RUN apk add --no-cache --virtual .gyp \
        python \
        make \
        g++ \
        git \
    && npm install \
    && apk del .gyp

# Frontend node_modules
WORKDIR /usr/src/app/frontend
# Install dependencies
COPY frontend/package.json ./
RUN npm install

# Bundle app source
WORKDIR /usr/src/app
COPY . ./

# Default to production mode
ENV NODE_ENV production
#ENV SWAGGER_ROOT_PATH
#ENV REACT_APP_API_PREFIX
#ENV REACT_APP_BASENAME
ENV PUBLIC_URL /

VOLUME /data
VOLUME /images

EXPOSE 3000

#CMD [ "npm", "start" ]
#TODO create entrypoint.sh
CMD npm run build-frontend && npm start

