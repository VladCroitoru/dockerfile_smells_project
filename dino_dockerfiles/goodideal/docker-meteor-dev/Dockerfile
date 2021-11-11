FROM ubuntu:16.04

MAINTAINER Jerry "jerry@wjz.im"

# build arguments
ARG APP_PACKAGES
ARG APP_LOCALE=en_US
ARG APP_CHARSET=UTF-8
ARG APP_USER=app
ARG APP_USER_DIR=/home/${APP_USER}
ARG METEOR_REL=2.5
ARG MONGO_REL=4.4.4

# run environment
ENV APP_PORT=${APP_PORT:-3000}
ENV APP_ROOT=${APP_ROOT:-/opt/application}

# exposed ports and volumes
EXPOSE $APP_PORT
VOLUME $APP_ROOT

# add packages for building NPM modules (required by Meteor)
RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl python git build-essential locales ${APP_PACKAGES}
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove
RUN DEBIAN_FRONTEND=noninteractive apt-get clean

RUN npm install -g pm2-meteor

# set the locale (required by Meteor)
RUN locale-gen ${APP_LOCALE}.${APP_CHARSET} &&\
    localedef ${APP_LOCALE}.${APP_CHARSET} -i ${APP_LOCALE} -f ${APP_CHARSET}

# add mongodb
RUN curl -O https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1604-${MONGO_REL}.tgz && \
    tar -zxvf mongodb-linux-x86_64-ubuntu1604-${MONGO_REL}.tgz && \
    mv mongodb-linux-x86_64-ubuntu1604-${MONGO_REL}/ /usr/local/mongodb && \
    rm -f mongodb-linux-x86_64-ubuntu1604-${MONGO_REL}.tgz && \
    mkdir -p /data/db

# create a non-root user that can write to /usr/local (required by Meteor)
ENV METEOR_ALLOW_SUPERUSER=1
#RUN useradd -mUd ${APP_USER_DIR} ${APP_USER}
#RUN chown -Rh ${APP_USER} /usr/local /data /opt/application

# add builds for gitlab ci
#RUN mkdir /builds && chown -Rh ${APP_USER} /builds

#USER ${APP_USER}

# install Meteor
RUN curl https://install.meteor.com/?release=${METEOR_REL} | sh

# run Meteor from the app directory
WORKDIR ${APP_ROOT}

# store mongodb data
VOLUME /data/db

# add docker entry
ADD docker-entry.sh /
ENTRYPOINT ["/docker-entry.sh"]

CMD ["meteor"]


