FROM hoangthienan/docker-nginx-php:latest

RUN apt-get update 
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y python-setuptools collectd python-pip

# Install supervisord
RUN easy_install supervisor

# install envtpl for replace
RUN pip install envtpl


# Copy startup script for getting environment information such as config...
ADD startup.sh      /var/startup.sh
RUN chmod +x /var/startup.sh


# collectd config
ADD collectd-config.conf.tpl /etc/collectd/configs/collectd-config.conf.tpl

# supervisord config
ADD supervisord.conf /etc/supervisord.conf

# create log directory for supervisord
RUN mkdir /var/log/supervisor/

# Create private folder for download config
RUN mkdir /var/www/private

CMD [ "/var/startup.sh" ]
