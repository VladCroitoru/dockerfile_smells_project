FROM mhart/alpine-node:6

MAINTAINER tobilg@gmail.com

# Set application name
ENV APP_NAME dcos-universe-browser

# Set application directory
ENV APP_DIR /usr/local/${APP_NAME}

# Set node env to production, so that npm install doesn't install the devDependencies
ENV NODE_ENV production

RUN apk update && \
    apk add git && \
    cd /usr/local && \
    git clone https://github.com/dcos-labs/dcos-universe-browser.git && \
    cd ${APP_DIR} && \
    npm set progress=false && \
    npm install bower -g && \
    bower install --allow-root --force-latest && \
    npm install --silent

# Change the workdir to the app's directory
WORKDIR ${APP_DIR}

CMD ["npm", "start"]