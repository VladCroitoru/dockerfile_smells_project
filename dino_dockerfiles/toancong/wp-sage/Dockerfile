FROM php:5.6

WORKDIR /usr/source/

ENV DEBIAN_FRONTEND noninteractive

# Add Node.js repo
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  curl \
  git \
  zip unzip \
  apt-transport-https \
  ca-certificates \
  && curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - \
  && echo "deb https://deb.nodesource.com/node_6.x jessie main" > /etc/apt/sources.list.d/nodesource.list \
# Install tools
  && apt-get update \
  && apt-get install --no-install-recommends -y \
  openssh-client \
  bzip2 \
  nodejs \
  && ln -f -s /usr/bin/nodejs /usr/bin/node \
# Slim down image
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

# Show versions
RUN php -v
RUN node -v
RUN npm -v

# Install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
  && composer global require hirak/prestissimo

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install -y yarn

# Install node tools
RUN npm install -g grunt-cli bower gulp
RUN grunt --version
RUN bower --allow-root --version
RUN gulp --version
RUN yarn --version

CMD ["bash"]
