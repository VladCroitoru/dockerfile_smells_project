FROM debian

RUN apt-get update && apt-get install -y cron supervisor munin munin-node nginx

EXPOSE 80

### APPLICATION CODE ###
# munin setup
RUN mkdir /var/run/munin && chown munin /var/run/munin
VOLUME /var/lib/munin

# munin-node setup
RUN sed -i 's/background 1/# background 1/g' /etc/munin/munin-node.conf
RUN sed -i 's/setsid 1/setsid 0/g' /etc/munin/munin-node.conf

### SUPPORTIVE SERVICES ###
ENV FILES_DIR ./container/files

# nginx setup
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf
ENV SITE_DEST /etc/nginx/sites-available/munin
COPY $FILES_DIR/$SITE_DEST $SITE_DEST
RUN ln -s $SITE_DEST /etc/nginx/sites-enabled/munin
RUN rm /etc/nginx/sites-enabled/default

# supervisor setup
COPY $FILES_DIR/etc/supervisor/conf.d /etc/supervisor/conf.d

### RUNNING IT OUT ###
CMD ["supervisord", "-n"]