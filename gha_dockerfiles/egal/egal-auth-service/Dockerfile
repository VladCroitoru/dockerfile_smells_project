FROM php:7.4.16-cli-buster

# Arguments defined in docker-compose.yml
ARG user=dev
ARG uid=1000

# Установить системные зависимости
RUN apt-get update && apt-get install -y \
    libpq-dev \
    curl \
    git \
    zip \
    unzip \
    procps

# Очистить кэш
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Установить расширения PHP
RUN docker-php-ext-install \
    pdo_mysql \
    sockets \
    pdo_pgsql \
    pcntl

#RUN docker-php-ext-enable \
#    pdo_mysql

# Получить последнюю версию Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Добавьте wait к изображению
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.8.0/wait /wait
RUN chmod +x /wait

# Create system user to run Composer and Artisan Commands
RUN useradd -G www-data,root -u $uid -d /home/$user $user
RUN mkdir -p /home/$user/.composer && \
    chown -R $user:$user /home/$user

WORKDIR /app

COPY . .

RUN composer install --no-interaction || (rm -rf vendor && composer install --no-interaction)
RUN chown -R $user:$user /app

USER $user

CMD /wait && ./artisan migrate --force && ./artisan egal:run
