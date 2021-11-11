FROM nginx:1.13
LABEL maintainer="Mars Hsu marshsu@gmail.com"

RUN apt-get update && apt-get install -y curl wget \
    && apt-get install -y gnupg gnupg2 gnupg1 \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install yarn

WORKDIR /var/www/default
