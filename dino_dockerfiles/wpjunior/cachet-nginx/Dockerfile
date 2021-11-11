FROM cachethq/docker:2.3.7

RUN sudo apt-get update
RUN sudo apt-get -q -y install nginx
ADD nginx.conf /etc/nginx/sites-enabled/cachet
RUN sudo mkdir /var/lib/nginx/body
RUN sudo sed -i 's/9000/3000/g' /etc/php5/fpm/pool.d/www.conf
ADD run.sh /sbin/run.sh

ENTRYPOINT ["/sbin/run.sh"]
