FROM ghost

# Update debian to work with postgres & s3
RUN echo 'deb http://security.debian.net testing/updates main\n' >> /etc/apt/sources.list
RUN apt-get update >/dev/null 2>/dev/null
RUN apt-get install -y s3cmd postgresql

# PM2 to start both ghost and the cron script
RUN npm install pm2@0.12.9 -g

# Copy the configuration for GHOST
ADD config.js /config.js
ENV GHOST_CONFIG /config.js

# Add the cron job for the backup scripts
ADD cron /cron
RUN cd /cron && npm i
ADD s3_backup.sh /s3_backup.sh
ADD s3_restore.sh /s3_restore.sh

# Make sure that the permissions & start scripts are in place
ADD ghost.sh /ghost.sh
RUN chown -R user /var/lib/ghost
RUN chmod +x /ghost.sh

ENTRYPOINT ["/entrypoint.sh"]

ENV NODE_ENV production
CMD ["/ghost.sh"]