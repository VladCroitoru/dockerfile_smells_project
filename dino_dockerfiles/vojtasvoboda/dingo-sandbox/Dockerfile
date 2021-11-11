# Use an official PHP runtime as a parent image
FROM php:7.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN apt-get update -y && apt-get install -y openssl zip unzip git
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install pdo mbstring
RUN composer install && composer build

# Run appplication when the container launches
CMD php artisan serve --host 0.0.0.0 --port=8000

# Make port 8000 available to the world outside this container
EXPOSE 8000

LABEL maintainer="vojtasvoboda.cz@gmail.com"
