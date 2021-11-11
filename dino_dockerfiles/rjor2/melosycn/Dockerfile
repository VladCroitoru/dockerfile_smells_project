FROM django

RUN apt-get update

########################################################################################################################
# NGINX

RUN apt-get install -y nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# symlink from the default config directory to your config file
RUN ln -s /code/app_nginx.conf /etc/nginx/sites-enabled/
########################################################################################################################

########################################################################################################################
# USWGI

RUN pip install uwsgi
# create a directory for the vassals
RUN mkdir /etc/uwsgi
RUN mkdir /etc/uwsgi/vassals
# symlink from the default config directory to your config file
RUN ln -s /code/app_uwsgi.ini /etc/uwsgi/vassals/
RUN mkdir /var/log/uwsgi
########################################################################################################################

########################################################################################################################
# SUPERVISOR
RUN apt-get install -y supervisor
RUN ln -s /code/supervisor-app.conf /etc/supervisor/conf.d/
########################################################################################################################

########################################################################################################################
# CODE
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
# ADD app/requirements.txt /code/app/
# RUN pip install -r app/requirements.txt
ADD . /code/
########################################################################################################################

########################################################################################################################
# DJANGO
RUN mkdir /var/log/django
WORKDIR /code/melosity
RUN python manage.py collectstatic --noinput
########################################################################################################################

cmd ["supervisord", "-n"]