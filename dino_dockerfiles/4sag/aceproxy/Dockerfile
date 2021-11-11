
# Version: 0.0.2

# Используем за основу контейнера phusion/baseimage
FROM ubuntu:14.04

# Переключаем Ubuntu в неинтерактивный режим — чтобы избежать лишних запросов
ENV DEBIAN_FRONTEND noninteractive 

# Устанавливаем локаль
RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales

# Устанавливаем время
RUN echo Asia/Yekaterinburg >/etc/timezone && dpkg-reconfigure -f noninteractive tzdata 

# Добавляем необходимые репозитарии и устанавливаем пакеты
RUN apt-get update && apt-get install -y wget
RUN echo 'deb http://repo.acestream.org/ubuntu/ trusty main' > /etc/apt/sources.list.d/acestream.list
RUN wget -O - http://repo.acestream.org/keys/acestream.public.key | apt-key add -
RUN apt-get update && apt-get install -y acestream-engine vlc-nox python-gevent supervisor ca-certificates git python-setuptools python-pip python-dev build-essential
RUN pip install greenlet gevent psutil

#
RUN mkdir -p /var/log/supervisor
RUN useradd --system --create-home --no-user-group --gid nogroup tv
RUN git clone https://github.com/AndreyPavlenko/aceproxy.git
RUN mv ./aceproxy /home/tv/aceproxy-master

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8000 8621 62062
VOLUME /etc/aceproxy

ENTRYPOINT ["/start.sh"]
