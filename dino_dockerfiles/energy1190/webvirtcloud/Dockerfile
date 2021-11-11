FROM ubuntu

RUN apt-get update && \
    apt-get -y install git \
    python-virtualenv \
    python-dev \
    python-pip \
    libxml2-dev \
    libvirt-dev \
    zlib1g-dev \
    nginx \
    supervisor \
    libsasl2-modules

RUN git clone https://github.com/retspen/webvirtcloud && \
    cp /webvirtcloud/conf/supervisor/webvirtcloud.conf /etc/supervisor/conf.d && \
    cp /webvirtcloud/conf/nginx/webvirtcloud.conf /etc/nginx/conf.d && \
    mv /webvirtcloud /srv

RUN chown -R www-data:www-data /srv/webvirtcloud && \
    virtualenv /srv/webvirtcloud/venv
    
RUN chmod +x /srv/webvirtcloud/venv/bin/activate && \
    /srv/webvirtcloud/venv/bin/activate && \
    pip install -r /srv/webvirtcloud/conf/requirements.txt
    
RUN python /srv/webvirtcloud/manage.py migrate && \
    chown -R www-data:www-data /srv/webvirtcloud && \
    rm /etc/nginx/sites-enabled/default
    
RUN service nginx restart && \
    service supervisor restart
