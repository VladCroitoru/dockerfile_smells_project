FROM debian:8

RUN echo "Europe/Berlin" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata
RUN apt-get update
RUN apt-get install -y curl git apt-transport-https zip


#Add dotdeb to apt
RUN echo 'deb http://packages.dotdeb.org jessie all' > /etc/apt/sources.list.d/dotdeb.list
RUN curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -
RUN apt-get update

#Install PHP & composer
RUN apt-get install -y php7.0 php7.0-mysql php7.0-curl php7.0-mbstring php7.0-bcmath php7.0-dom php7.0-zip
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer


#Install Surf
ADD surf.phar /usr/local/bin/surf
RUN chmod +x /usr/local/bin/surf


#Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
