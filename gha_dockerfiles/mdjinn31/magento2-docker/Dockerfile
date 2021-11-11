FROM ubuntu
LABEL maintainer="Jonathan Rivera <mdjinn31@gmail.com>" 

# Instalacion Basica del contenedor
ENV TZ=America/Guatemala \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install tzdata


RUN apt-get -y install git wget curl nano unzip apt-transport-https software-properties-common certbot


# Configurando SSH
RUN apt-get -y install openssh-server
RUN service ssh start

# Intsalando Apache 2 como servidor web
RUN apt-get -y install apache2
RUN service apache2 start
RUN a2enmod rewrite
RUN rm -rf /etc/apache2/apache2.conf
COPY configs/apache2.conf /etc/apache2/
RUN service apache2 restart
RUN chmod go-rwx /var/www/html
RUN chmod go+x /var/www/html

# Instalando PHP como interprete 
RUN apt-get -y update
RUN apt-get -y install php php-cli php-fpm php-json php-common php-mysql php-zip php-gd php-mbstring php-curl php-xml php-pear php-bcmath

# Instalando Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer -v

# Instalando Webmin para administrar el contenedor
RUN apt-get upgrade -y
RUN wget -q http://www.webmin.com/jcameron-key.asc -O- | apt-key add -
RUN add-apt-repository "deb [arch=amd64] http://download.webmin.com/download/repository sarge contrib"
RUN apt-get update

RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes
RUN apt-get purge apt-show-versions
RUN rm /var/lib/apt/lists/*lz4
RUN apt-get -o Acquire::GzipIndexes=false update
RUN apt-get -y install apt-show-versions
RUN apt-get -y install webmin
RUN /etc/init.d/webmin start
RUN /usr/share/webmin/changepass.pl /etc/webmin root root
RUN service apache2 start

# Levantamos e iniciamos el servidorStart
EXPOSE 80 10000 443
RUN cd /sbin
RUN touch run.sh
RUN echo "#!/bin/bash" >> run.sh
RUN echo "while /bin/true; do" >> run.sh
RUN echo "service webmin start" >> run.sh
RUN echo "service apache2 start" >> run.sh
RUN echo "sleep 60" >> run.sh
RUN echo "done" >> run.sh
RUN chmod +x run.sh
ENTRYPOINT ["./run.sh"]