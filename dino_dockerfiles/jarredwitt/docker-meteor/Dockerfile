FROM node:4.4.7

RUN apt-get update

RUN npm update -g npm
RUN apt-get install g++ gyp

# Make sure we have a directory for the application
RUN mkdir -p /var/www
RUN chown -R www-data:www-data /var/www

# Install fibers -- this doesn't seem to do any good, for some reason
RUN npm install -g fibers

# Install Meteor
#RUN curl https://install.meteor.com/ |sh

# Install entrypoint
ADD entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh

# Add known_hosts file
ADD known_hosts /root/.ssh/known_hosts

EXPOSE 80

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
CMD []

