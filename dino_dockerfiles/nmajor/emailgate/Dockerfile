FROM node:8.11.3

RUN sed -i '/jessie-updates/d' /etc/apt/sources.list

RUN apt-get -o Acquire::Check-Valid-Until=false update -qq
RUN apt-get install -y bzip2
RUN apt-get install -y libfontconfig
RUN apt-get install -y nginx
RUN apt-get install -y supervisor
RUN mkdir -p /var/log/nginx /var/log/supervisor

# Download and install phantomjs
WORKDIR /tmp
RUN wget https://us-east.manta.joyent.com//nmajor/public/emailgate/container/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /bin/

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD package.json /tmp/package.json
RUN cd /tmp && npm install --production
RUN npm -g install webpack@1.13.0

ADD container/containerbuddy/containerbuddy /sbin/containerbuddy
ADD container/nginx.conf /etc/nginx/nginx.conf
ADD container/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV APP_HOME /var/app
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME
ADD . $APP_HOME
RUN touch ./.env
RUN ln -sfF /tmp/node_modules $APP_HOME/node_modules
RUN npm run build-server

RUN webpack -p --config webpack.config.prod.js

EXPOSE 80
CMD ["/usr/bin/supervisord"]
