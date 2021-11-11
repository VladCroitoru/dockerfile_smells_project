#Basic Image
FROM ubuntu:14.04
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
#RUN apt-get install -y --force-yes git
RUN apt-get install -y --force-yes nginx
RUN apt-get install -y --force-yes build-essential
RUN apt-get install -y --force-yes python-pip
RUN apt-get install -y --force-yes libblas-dev liblapack-dev gfortran libfreetype6-dev libpng-dev python-dev libxft-dev libpq-dev

#Create the folder where app lives
#Assumes the entirety of my app is there
RUN mkdir /var/www
RUN mkdir /var/www/groupdynamics
WORKDIR /var/www/groupdynamics
ADD ./requirements.txt /var/www/groupdynamics/requirements.txt
RUN pip install -r requirements.txt
ADD . /var/www/groupdynamics

#install Supervisor
RUN apt-get install -y --force-yes supervisor
RUN ln -s /var/www/groupdynamics/config/supervisor.conf /etc/supervisor/conf.d/

#Set nginx config
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /var/www/groupdynamics/config/nginx.conf /etc/nginx/conf.d
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#Set uwsgi config
RUN mkdir -p /var/log/uwsgi
RUN mkdir /etc/uwsgi
RUN mkdir /etc/uwsgi/vassals
RUN ln -s /var/www/groupdynamics/config/uwsgi.ini /etc/uwsgi/vassals
RUN chown -R www-data:www-data /var/log/uwsgi
RUN chown -R www-data:www-data /var/www

ENV NEW_RELIC_CONFIG_FILE=/var/www/groupdynamics/config/newrelic.ini

EXPOSE 80
CMD ["supervisord", "-n"]