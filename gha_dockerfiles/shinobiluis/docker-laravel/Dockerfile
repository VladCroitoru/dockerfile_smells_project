FROM php:7.4.21-apache                                                                                                                                                                                     
# Actualizaciones de linux
RUN apt-get update
RUN apt-get upgrade -y
# # Instalamos wget
RUN apt-get install wget -y
RUN apt-get install -y iputils-ping
# Instalamos zsh
RUN apt-get install zsh -y
RUN apt-get install git-core -y
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
RUN chsh -s `which zsh`
RUN apt-get install vim -y
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
RUN echo "source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc
 
# Instalamos lo necesario para php
ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/
RUN chmod +x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions gd mysqli ldap zip pdo_mysql
 
####################################################
############ Instalar extensiones php  #############
####################################################
# Más información ver en: https://hub.docker.com/_/php
# Buscar el apartado: How to install more PHP extensions
# Abajo se coloca un ejemplo de la instalacion de mysqli
# RUN docker-php-ext-install mysqli
# RUN docker-php-ext-configure ldap
# RUN docker-php-ext-install ldap
 
####################################################
############### Intalamos composer #################
####################################################
# Copiamos esl archivo de scripst dentro del docker
COPY ./instalaciones/install_composer.sh  /tmp
# Nos movemos a la carpeta tempora
WORKDIR /tmp
# Ejecutamos el script que intala java 1.8
RUN sh ./install_composer.sh
 
#Regresamos a la carpeta del proyecto
WORKDIR /var/www/html
 
# convertimos el ini de produccion
RUN mv "$PHP_INI_DIR/php.ini-production" "$PHP_INI_DIR/php.ini"
####################################################
########## Instalamos modulos de apache ############
####################################################
RUN a2enmod rewrite

####################################################
############ Dejamos corriendo apache  #############
####################################################
CMD apachectl -D FOREGROUND 
