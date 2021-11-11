FROM phusion/baseimage:0.9.19
MAINTAINER QAutomatron

# Default variables
ENV YANDEX_FOLDER = "/var/lib/selenium"

# Install sudo and wget
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -yqq
RUN apt-get install sudo -yqq
RUN apt-get install wget -yqq

# Will install yandex-disk
RUN echo "deb http://repo.yandex.ru/yandex-disk/deb/ stable main" | tee -a /etc/apt/sources.list.d/yandex.list > /dev/null && wget http://repo.yandex.ru/yandex-disk/YANDEX-DISK-KEY.GPG -O- | apt-key add - && apt-get update && apt-get install -y yandex-disk

# Will create folder
RUN mkdir /var/lib/selenium

# Folder to mount
VOLUME ["/var/lib/selenium"]

# Copy start script
COPY start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]
