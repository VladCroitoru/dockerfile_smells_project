FROM wordpress

RUN apt-get update && apt-get install -y \
        librecode-dev \
        libmcrypt-dev \
    && docker-php-ext-install -j$(nproc) recode mcrypt 
