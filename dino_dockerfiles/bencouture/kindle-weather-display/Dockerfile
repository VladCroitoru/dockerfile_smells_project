FROM phusion/baseimage:0.9.16

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#Install dependencies
RUN apt-get update
RUN apt-get install -y python cron lighttpd librsvg2-bin pngcrush

#Add files
RUN mkdir /www
RUN mkdir /www/root
ADD ./server /www

#Set up cron job for updating weather forecast
RUN crontab -l | { cat; echo "25,55 * * * * /www/weather-script.sh"; } | crontab -

#Run script once initially
RUN /www/weather-script.sh

#Run web server
CMD /usr/sbin/lighttpd -D -f /www/lighttpd.conf