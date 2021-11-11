FROM ubuntu
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt -y install \
      software-properties-common \
      apt-transport-https \
      ca-certificates \
      openssh-client \
      git \
      curl \
      wget \
      unzip \
      socat \
      neovim \
      gnupg \
      lsb-release \
    && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && add-apt-repository ppa:ondrej/php \
    && apt-get update \
    && apt-get -y install --no-install-recommends \
      docker-ce \
      docker-ce-cli \
      containerd.io \
      php8.0 \
      php8.0-cli \
      php8.0-fpm \
      php8.0-common \
      php8.0-mysql \
      php8.0-gd \
      php8.0-intl \
      php8.0-zip \
      php8.0-curl \
      php8.0-xml \
      php8.0-mbstring \
    && sed -i "s/\;date\.timezone =/date\.timezone = America\/Chicago/" /etc/php/8.0/cli/php.ini \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php -r "if (hash_file('sha384', 'composer-setup.php') === '906a84df04cea2aa72f40b5f787e49f22d4c2f19492ac310e8cba5b96ac8b64115ac402c8cd292b8a03482574915d1a8') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" \
    && php composer-setup.php \
    && php -r "unlink('composer-setup.php');" \
    && mv composer.phar /usr/local/bin/composer \
    && curl -fsSL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get -y install nodejs \
    && npm install -g yarn \
    && curl https://kr.gx.ag | sh