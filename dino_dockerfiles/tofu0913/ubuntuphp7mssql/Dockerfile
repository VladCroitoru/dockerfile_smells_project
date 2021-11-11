FROM ubuntu:16.04
MAINTAINER Cliff Chen<tofu0913 (at) gmail (dot) com>

RUN apt-get update 
RUN apt-get -y install wget net-tools curl apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-server.list > /etc/apt/sources.list.d/mssql-server.list
RUN apt-get -y install php7.0 libapache2-mod-php7.0 mcrypt php7.0-mcrypt php-mbstring php-pear php7.0-dev apache2 php7.0-gd php7.0-curl php7.0-zip 
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-tools.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN apt-get install -y unixodbc-dev
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
#RUN source ~/.bashrc
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8

RUN pecl install sqlsrv pdo_sqlsrv
RUN echo 'extension=sqlsrv.so' >> /etc/php/7.0/apache2/php.ini
RUN echo 'extension=pdo_sqlsrv.so' >> /etc/php/7.0/apache2/php.ini
EXPOSE 80

CMD service apache2 start && tail -F /var/log/apache2/error.log
