############
# Frontend #
############
# Use Node as the base image to build our frontend
FROM node:lts AS frontend

# Set THEME_NAME as build argument
ARG THEME_NAME

# Set the work directory to /usr/src/app so all subsequent commands in this file start from the /usr/src/app directory
# Also set this work directory so everytime we use docker exec -it showpad/analytics-backend bash, we automatically end
# up in this directory
RUN mkdir -p /app/src/Frontend/Themes/$THEME_NAME
WORKDIR /app/src/Frontend/Themes/$THEME_NAME

# Copy the files needed to retrieve the dependencies. It's important to separate dependency retrieval from adding code.
# Dependencies usually don't change a lot (at least not on every build). Therefore it's important to use Docker's layers
# to automatically cache dependencies
COPY src/Frontend/Themes/$THEME_NAME/.npmrc .
COPY src/Frontend/Themes/$THEME_NAME/package.json .
COPY src/Frontend/Themes/$THEME_NAME/package-lock.json .

# Since npm 5.7.0, the new npm ci command is introduced that installs ONLY from the lock-file.
# Beyond guaranteeing you that you'll only get what is in your lock-file it's also much faster (2x-10x!) than
# npm install when you don't start with a node_modules. It is also more strict than a regular install, which can help
# catch errors or inconsistencies caused by the incrementally-installed local environments of most npm users.
RUN npm ci

# Copy the code. Important here is that copying is done based on the rules defined in the .dockerignore file.
# That files uses a DENY all strategy where by default no files/folders are part of the copy unless those specified in
# the .dockerignore file. This allows builds to be light and prevents any files to be accidentally used as part of the
# build e.g. secrets, log files, etc...
COPY src/Frontend/Themes/$THEME_NAME .

# Compile typescript to a dist folder. In production, we serve the compiled javascript from the dist folder.
# Generate sourcemaps to send to Sentry for a better error stacktrace.
RUN npm run build

# Make sure to copy the CSS to a Core/Layout/Css/screen.css file. This gets autoloaded in the CMS by CKEditor.
RUN mkdir -p Core/Layout/Css && cp dist/assets/app.*.css Core/Layout/Css/screen.css

##################
# Backend app    #
##################
FROM php:7.4-apache

# Enable Apache mod_rewrite
RUN a2enmod rewrite

# Install mysql and mysqladmin binaries
RUN apt-get update && apt-get install -y --no-install-recommends mariadb-client
COPY --from=mariadb:10 /usr/bin/mysqladmin /usr/local/bin/mysqladmin

# Install GD2
RUN apt-get update && apt-get install -y --no-install-recommends --allow-downgrades \
    libonig-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libz-dev \
    zlib1g-dev \
    libpng-dev && \
    docker-php-ext-configure gd --with-freetype=/usr/include/ --with-jpeg=/usr/include/ && \
    docker-php-ext-install -j$(nproc) gd && \
    rm -rf /var/lib/apt/lists/*

# Install pdo_mysql & mbstring
RUN docker-php-ext-install pdo_mysql mbstring

# Install zip & unzip
RUN apt-get update && apt-get install -y libzip-dev zip && \
    docker-php-ext-install zip && \
    rm -rf /var/lib/apt/lists/*

# Install intl
RUN apt-get update && apt-get install -y --no-install-recommends \
    g++ \
    libicu-dev \
    zlib1g-dev && \
    docker-php-ext-configure intl && \
    docker-php-ext-install intl && \
    rm -rf /var/lib/apt/lists/*

# Enable pcov for test coverage
RUN pecl install pcov && \
    docker-php-ext-enable pcov

# Install yq (a YAML processor). We need this to write to our parameters.yml in the entrypoint.
RUN apt-get update && apt-get install -y wget && \
    wget -O /usr/local/bin/yq https://github.com/mikefarah/yq/releases/download/v4.13.3/yq_linux_amd64 && \
    chmod 777 /usr/local/bin/yq

# Install Composer 2
RUN curl -sS https://getcomposer.org/installer | \
    php -- --install-dir=/usr/bin/ --filename=composer

# Set the work directory to /var/www/html so all subsequent commands in this file start from that directory.
# Also set this work directory so that it uses this directory everytime we use docker exec.
WORKDIR /var/www/html

# Download Fork CMS as base to test our module
RUN curl -sL https://github.com/forkcms/forkcms/archive/5.10.0.tar.gz | tar xz --strip-components 1

# Install the Fork CMS composer dependencies
RUN composer install --prefer-dist --no-dev --no-scripts --no-progress

# Copy our repository files into the container.
ARG THEME_NAME
COPY . /var/www/html
COPY --from=frontend /app/src/Frontend/Themes/$THEME_NAME/dist ./src/Frontend/Themes/$THEME_NAME/dist
COPY --from=frontend /app/src/Frontend/Themes/$THEME_NAME/Core ./src/Frontend/Themes/$THEME_NAME/Core

# Give apache user write access
RUN chown -R www-data:www-data /var/www/html/src/*/Cache /var/www/html/src/*/Files /var/www/html/var

# Set health check to see if container is still doing fine
HEALTHCHECK --interval=10s --timeout=3s --retries=3  CMD curl -f http://127.0.0.1:80|| exit 1

# This specifies on which port the application will run. This is pure communicative and makes this 12 factor app compliant
# (see https://12factor.net/port-binding).
EXPOSE 80 443

# Define our entrypoint script that will setup the container when it boots up
ENTRYPOINT ["deploy/docker-entrypoint.sh"]
