FROM node:11-stretch

# Https repositories support.
RUN apt-get update
RUN apt-get install apt-transport-https

RUN wget -q -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

RUN apt-get update
RUN apt-get install -y \
    google-chrome-stable \
    mongodb \
    python-dev \
    python-pip \
    python3-dev \
    python3-pip \
    redis-server \
    ruby-dev \
    rubygems \
    yarn

RUN gem install dpl
RUN yarn global add heroku
RUN heroku --version

RUN easy_install --upgrade pip
RUN easy_install virtualenv
RUN pip install pipenv
