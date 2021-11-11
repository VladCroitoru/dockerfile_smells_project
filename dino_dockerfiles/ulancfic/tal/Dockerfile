FROM ubuntu:14.04
RUN apt-get dist-upgrade
RUN apt-get -y update
RUN apt-get install -y git
RUN apt-get install -y apache2
RUN apt-get install -y php5 --fix-missing
RUN apt-get install -y libapache2-mod-php5
RUN apt-get install -y php5-mcrypt
RUN service apache2 stop
EXPOSE 80
WORKDIR /var/www/
RUN git clone --recursive https://github.com/ULANCFIC/tal.git
RUN sed -i "s/DocumentRoot\ \/var\/www\/html/DocumentRoot\ \/var\/www\/tal/g" /etc/apache2/sites-available/000-default.conf
CMD /usr/sbin/apache2ctl -D FOREGROUND

# for testing:
# curl http://[HOST]/
