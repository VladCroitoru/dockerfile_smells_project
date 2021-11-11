FROM ubuntu:14.04
MAINTAINER Jeremy Pollock <jpollock911@gmail.com>

RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get install -y build-essential git nginx supervisor bcrypt libssl-dev libffi-dev libpq-dev vim redis-server rsyslog wget nodejs npm

# stop supervisor service as we'll run it manually
RUN service supervisor stop
RUN mkdir /var/log/node
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

WORKDIR /code/

# Add service.conf
ADD ./files/service.conf /code/
RUN ln -s /code/service.conf /etc/nginx/sites-enabled/

# Add supervisor
ADD ./files/supervisord.conf /code/
RUN ln -s /code/supervisord.conf /etc/supervisor/conf.d/


RUN ln -s /usr/bin/nodejs /usr/bin/node

# Install bower
RUN npm install -g bower

COPY src/package.json /src/package.json
RUN cd /src; npm install

COPY src/bower.json /src/bower.json
RUN cd /src; bower install --allow-root


# Bundle app source
COPY src /src/

# Add github repo code to code file
ADD . /code/
RUN mkdir /code/logs

# expose port(s)
EXPOSE 80
EXPOSE 443

CMD ./run_service.sh



