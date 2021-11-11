FROM debian:jessie
MAINTAINER Daniel Blackhall <dblackhall@gmail.com>
#Steps to follow are here: http://docs.brewpi.com/manual-brewpi-install/manual-brewpi-install.html

EXPOSE 80

RUN apt-get update && apt-get -y install git python python-dev python-pip cron sudo



#Step 1 Installing lemp server
RUN apt-get -y install \
	nginx \
	php5 \
	php5-fpm

RUN rm -rf /var/www/*

RUN mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bak
COPY nginx-config /etc/nginx/sites-available/default



#Step 2 Installing python requirements
RUN pip install pyserial simplejson configobj psutil gitpython
RUN apt-get -y install arduino-core



#Step 3 Setting up users and permissions
RUN useradd -m -k /dev/null -G www-data,dialout brewpi
RUN echo 'brewpi:worstpasswordever' | chpasswd

RUN chown -R www-data:www-data /var/www
RUN chown -R brewpi:brewpi /home/brewpi
RUN find /home/brewpi -type f -exec chmod g+rwx {} \;
RUN find /home/brewpi -type d -exec chmod g+rwxs {} \;
RUN find /var/www -type d -exec chmod g+rwxs {} \;
RUN find /var/www -type f -exec chmod g+rwx {} \;
RUN /home/brewpi/utils/fixPermissions.sh



#Step 4 Using git for BrewPi
RUN git clone --branch legacy --depth 1 https://github.com/BrewPi/brewpi-script /home/brewpi
RUN git clone https://github.com/BrewPi/brewpi-www /var/www



#Step 5 Modifying BrewPi config files
COPY brewpi-config.cfg /home/brewpi/settings/config.cfg



#Step 6 Cron Job
COPY brewpi-crontab /etc/cron.d/brewpi
RUN chmod 0644 /etc/cron.d/brewpi



#Customised serial over wifi changes
RUN sed -i.bak "s#ser = serial.Serial(port, baudrate=baud_rate, timeout=time_out, write_timeout=0)#ser = serial.serial_for_url(port, baudrate=baud_rate, timeout=0.6, write_timeout=0.6)#" /home/brewpi/BrewPiUtil.py



# Start the cron daemon shell
COPY configure-and-start.sh configure-and-start.sh
RUN chmod +x configure-and-start.sh
CMD ./configure-and-start.sh

