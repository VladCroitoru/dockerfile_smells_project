FROM php:latest

# install curl, git, and rsync
RUN apt-get -y update && apt-get install -y curl git rsync

# install Node.js LTS and Yarn
RUN curl -sL 'https://deb.nodesource.com/setup_12.x' | bash /dev/stdin
RUN curl -sS 'https://dl.yarnpkg.com/debian/pubkey.gpg' | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get -y update && apt-get install -y nodejs yarn

# install WP-CLI
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp
