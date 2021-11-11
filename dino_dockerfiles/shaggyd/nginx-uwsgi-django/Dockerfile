FROM ubuntu:14.04

# Install Python
RUN apt-get update && apt-get install python python-setuptools python-dev gcc supervisor nginx -y

# Install Uwsgi and Supervisor
RUN easy_install pip && pip install uwsgi

# Create source direcotry
RUN mkdir -p /etc/container/ &&  mkdir -p /opt/application/
ADD . /etc/container/

# Clean up default NGINX
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && rm /etc/nginx/sites-enabled/default

# Configure NGINX and Supervisor
RUN ln -sf /etc/container/django.conf /etc/nginx/sites-enabled/ && ln -sf /etc/container/supervisor.conf /etc/supervisor/conf.d/


# Set the container envs
ENV APPLICATION='application'

EXPOSE 80
EXPOSE 443

ADD ./startup.sh /bin/
CMD ["/bin/startup.sh"]

# Redirect logs
#RUN /bin/sh -c "ln -sf /dev/stdout /var/log/access.log && ln -sf /dev/stderr /var/log/nginx/error.log"
