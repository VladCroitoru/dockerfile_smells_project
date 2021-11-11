FROM php:latest

# install curl and git
RUN apt-get -y update && apt-get install -y curl git php5-cli

# install Node.js LTS
RUN curl -sL 'https://deb.nodesource.com/setup_6.x' | bash /dev/stdin

# install yarn package manager
RUN curl -sS 'https://dl.yarnpkg.com/debian/pubkey.gpg' | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get -y update && apt-get install -y nodejs yarn python python-setuptools python-dev build-essential libssl-dev

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# install ansible
RUN easy_install pip
RUN pip install ansible
