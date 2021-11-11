FROM shadowbane/feeder-debian:9.11

MAINTAINER Adli I. Ifkar <adly.shadowbane@gmail.com>

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE /var/run/apache2/httpd.pid
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/www

# Download installer
RUN mkdir /feeder
WORKDIR /feeder
RUN wget -c https://siakad-btp.s3.ap-southeast-1.amazonaws.com/feeder/feeder.tar.gz -O source.tar.gz

# Extracting source
RUN tar -xzvf source.tar.gz

# Extracting Installer
RUN cd /feeder/feeder/32 \
    && unzip Feeder_3.2_Amd64_Debian.zip \
    && chmod +x INSTALL

# Extracting Patch 3,3
RUN cd /feeder/feeder/33 \
    && unzip Patch_3.3_Amd64_Linux.zip \
    && chmod +x UPDATE_PATCH.3.3

# Extracting Patch 3,4
RUN cd /feeder/feeder/34 \
    && unzip Patch_3.4_Amd64_Linux.zip \
    && chmod +x UPDATE_PATCH.3.4

# Extracting Patch 4,0
RUN cd /feeder/feeder/40 \
    && unzip Patch_4.0_Amd64_Linux.zip \
    && chmod +x UPDATE_PATCH.4.0

# Extracting Patch 4,1
RUN cd /feeder/feeder/41 \
    && unzip Patch_4.1_Amd64_Linux.zip \
    && chmod +x UPDATE_PATCH.4.1

## Installing Feeder
WORKDIR /feeder/feeder/32
RUN ./INSTALL

## Patching 3.3
WORKDIR /feeder/feeder/33
RUN ./UPDATE_PATCH.3.3

## Patching 3.4
WORKDIR /feeder/feeder/34
RUN ./UPDATE_PATCH.3.4

## Patching 4.0
WORKDIR /feeder/feeder/40
RUN ./UPDATE_PATCH.4.0

## Patching 4.1
WORKDIR /feeder/feeder/41
RUN ./UPDATE_PATCH.4.1

## Patching postgresql
RUN tar zxfv /feeder/postgresql/postgresql.tar.gz -C /var/lib

# Cleanup
WORKDIR /var/www/html
RUN rm -rf /feeder/feeder*

# copy run script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Exposing web ports
EXPOSE 8082

WORKDIR /var/www/html
CMD ["/run.sh"]
