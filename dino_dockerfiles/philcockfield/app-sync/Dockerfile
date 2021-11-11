FROM philcockfield/node-pm2


# PM2: auto-rotate logs.
# See: https://github.com/pm2-hive/pm2-logrotate
RUN pm2 install pm2-logrotate
RUN pm2 set pm2-logrotate:max_size 10MB
RUN pm2 set pm2-logrotate:interval_unit 'DD'
RUN pm2 set pm2-logrotate:interval 1
RUN pm2 set pm2-logrotate:retain 7


# Gulp (in case any downloaded apps try to use it).
RUN npm install -g gulp


# Install NPM modules.
#
# NOTE: This is done prior to copying the working folder to prevent a rebuild
#       of the modules on each file change (uses cache instead).
#
# See: http://bitjudo.com/blog/2014/03/13/building-efficient-dockerfiles-node-dot-js/
#
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/


# Copy working files.
WORKDIR /opt/app
COPY . /opt/app


EXPOSE 80
CMD ["npm", "start"]
