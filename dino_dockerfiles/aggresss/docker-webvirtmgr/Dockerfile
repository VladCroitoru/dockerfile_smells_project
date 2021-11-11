FROM ubuntu:14.04
MAINTAINER Jagger Yu <aggresss@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

# Modify apt-get to aliyun mirror
RUN sed -i 's/archive.ubuntu/mirrors.aliyun/g' /etc/apt/sources.list
RUN apt-get -y update

# Modify timezone to GTM+8
ENV TZ=Asia/Shanghai
RUN apt-get -y install tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Modify locale
RUN apt-get -y install locales
RUN locale-gen en_US.UTF-8
RUN echo "LANG=\"en_US.UTF-8\"" > /etc/default/locale && \
    echo "LANGUAGE=\"en_US:en\"" >> /etc/default/locale && \
    echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale

# Modify pip mirror
RUN mkdir -p /root/.pip
RUN echo "[global]" > /root/.pip/pip.conf && \
    echo "index-url=http://mirrors.aliyun.com/pypi/simple/" >> /root/.pip/pip.conf && \
    echo "[install]" >> /root/.pip/pip.conf && \
    echo "trusted-host=mirrors.aliyun.com" >> /root/.pip/pip.conf


RUN apt-get -y install git python-pip python-libvirt python-libxml2 supervisor novnc nginx 

RUN git clone https://github.com/retspen/webvirtmgr
WORKDIR /webvirtmgr
RUN pip install -r requirements.txt
ADD local_settings.py /webvirtmgr/webvirtmgr/local/local_settings.py
RUN /usr/bin/python /webvirtmgr/manage.py collectstatic --noinput

ADD supervisor.webvirtmgr.conf /etc/supervisor/conf.d/webvirtmgr.conf
ADD nginx.webvirtmgr.conf /etc/nginx/sites-available/webvirtmgr

ADD bootstrap.sh /webvirtmgr/bootstrap.sh

RUN mkdir /var/local/webvirtmgr
RUN chown www-data:www-data -R /webvirtmgr
RUN chown www-data:www-data -R /var/local/webvirtmgr

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN ln -s /etc/nginx/sites-available/webvirtmgr /etc/nginx/sites-enabled
RUN apt-get -ys clean

WORKDIR /
VOLUME /var/local/webvirtmgr

EXPOSE 8080/tcp 6080/tcp
CMD ["supervisord", "-n"] 
