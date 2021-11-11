FROM cypress/internal:cy-0.19.4

MAINTAINER Gabor Raz

USER root

RUN apt-get update \
    # Install yarn
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    # Install Meteor
    && curl https://install.meteor.com/ | sh \
    && apt-get install -y openssh-client \
    && echo 'PATH="/usr/local/node/bin:${PATH}"' >> /etc/bash.bashrc \
    # set locale for mongo db
    && apt-get install -y locales >/dev/null \
    && echo "en_US UTF-8" > /etc/locale.gen \
    && locale-gen en_US.UTF-8 \
    && export LANG=en_US.UTF-8 \
    && export LANGUAGE=en_US:en \
    && export LC_ALL=en_US.UTF-8