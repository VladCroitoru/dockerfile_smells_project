FROM nginx:mainline
MAINTAINER Thinegan Ratnam <thinegan@thinegan.com>

RUN apt-get update && apt-get install -y supervisor
RUN apt-get install -y python-pip && pip install supervisor-stdout
RUN apt-get install -y openssl bzip2 zip libssl-dev

RUN mkdir -p /etc/nginx/sites-available
RUN mkdir -p /etc/nginx/sites-enabled

RUN mkdir -p /home/www/public_html/dev.timeclone.com
RUN chown -R www-data:www-data /home/www/public_html/dev.timeclone.com
RUN chmod -R +x /home/www/public_html/dev.timeclone.com

ADD config/nginx.conf /etc/nginx/nginx.conf
ADD config/proxy.conf /etc/nginx/proxy.conf
ADD config/dev.timeclone.com /etc/nginx/sites-available/dev.timeclone.com

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

RUN ln -sf /etc/nginx/sites-available/dev.timeclone.com /etc/nginx/sites-enabled/
ADD supervisord.conf /etc/supervisor/supervisord.conf
ADD supervisor-config/nginx.sv.conf /etc/supervisor/conf.d/

EXPOSE 80 443
# Define default command
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]
