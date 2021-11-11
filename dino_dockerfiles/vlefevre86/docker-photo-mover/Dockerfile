FROM node:0.10.46

ENV APTLIST="git cron"

RUN apt-get update -q && \
apt-get install $APTLIST -qy && \
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

#Adding Custom files
ADD tasks/ /tasks/
ADD init/ /etc/my_init.d/
VOLUME /orig /dest
RUN chmod -v +x /etc/my_init.d/*.sh /tasks/*.sh
RUN /etc/my_init.d/30_update_Photo-Mover.sh

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron
 
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/hello-cron
 
# Create the log file to be able to run tail
RUN touch /tasks/cron.log
 
# Run the command on container startup
CMD cron && tail -f /tasks/cron.log
