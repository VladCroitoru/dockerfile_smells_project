FROM php:7.0-apache

ENV DEBIAN_FRONTEND=noninteractive

# Installing MySql without root password; installing Ruby with Sass 
RUN apt-get update && apt-get install -y curl \
net-tools mysql-server && \
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 && \
curl -sSL https://get.rvm.io | bash -s stable --ruby --gems=sass && \
/usr/sbin/a2enmod rewrite



