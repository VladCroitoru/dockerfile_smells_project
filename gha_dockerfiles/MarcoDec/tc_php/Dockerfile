FROM php:8.0-fpm

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt upgrade -y --no-install-recommends && \
    apt autoremove -y && \
    apt install -y --no-install-recommends apt-utils debconf

RUN apt install -y --no-install-recommends \
        cron \
        cups-client \
        fontconfig \
        g++ \
        git \
        gnupg2 \
        graphviz \
        libicu-dev \
        libjpeg62-turbo \
        libmagickwand-dev \
        libpng-dev \
        libreoffice \
        libx11-6 \
        libxcb1 \
        libxext6 \
        libxrender1 \
        libzip-dev \
        locales \
        poppler-utils \
        sudo \
        xfonts-75dpi \
        xfonts-base \
        xfonts-utils \
        unzip \
        wget \
        zsh \
        zip \
        zlib1g-dev && \
    pecl install imagick && \
    chsh -s /usr/bin/zsh root && \
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh && \
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting && \
    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    docker-php-ext-configure intl && \
    docker-php-ext-install \
        calendar \
        gd \
        intl \
        pdo_mysql \
        zip && \
    curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
    wget https://get.symfony.com/cli/installer -O - | bash && \
    mv /root/.symfony/bin/symfony /usr/local/bin/symfony &&\
    rm -r /root/.symfony/ && \
    curl -fsSL https://deb.nodesource.com/setup_current.x | bash - && \
    apt install -y nodejs && \
    npm install -g yarn && \
    echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen && \
    locale-gen && \
    wget --no-check-certificate https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.stretch_amd64.deb && \
    dpkg -i "wkhtmltox_0.12.6-1.stretch_amd64.deb" && \
    apt-get -f install && \
    apt upgrade -y --no-install-recommends && \
    apt autoclean -y && \
    apt autoremove -y && \
    echo 'root:root' | chpasswd # Mot de passe root : root

ADD entrypoint.sh /usr/local/bin/docker-php-entrypoint
