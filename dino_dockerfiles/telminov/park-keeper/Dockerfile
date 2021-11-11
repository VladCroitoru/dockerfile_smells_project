# docker build -t telminov/park-keeper .
# docker run --rm -ti --name parkkeeper --link mongo3:mongo3 -p 8080-8081:8080-8081 -p 5548-5552:5548-5552 --volume=/var/docker/park-keeper/conf/:/conf/ --volume=/var/docker/park-keeper/data/:/data/ telminov/park-keeper

FROM telminov/ubuntu-14.04-python-3.5
MAINTAINER telminov <telminov@soft-way.biz>

# web server web socket server
EXPOSE 8080-8081
# zmq ports
EXPOSE 5548-5552

# directory for sqlite3 database
VOLUME /data/
# django settings and frontend config
VOLUME /conf/
# frontend static for webserver
VOLUME /frontend/

RUN apt-get update && \
    apt-get install -y \
                    vim \
                    curl \
                    build-essential \
                    git \
                    supervisor

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

RUN mkdir /var/log/park-keeper

# copy source
COPY . /opt/park-keeper
WORKDIR /opt/park-keeper

# install frontend
WORKDIR /opt/park-keeper/frontend
RUN npm install
RUN node_modules/.bin/bower install --allow-root --config.interactive=false
RUN node_modules/.bin/gulp build

# install backend
WORKDIR /opt/park-keeper/backend
RUN pip3 install -r requirements.txt
RUN cp project/settings.sample.py project/settings.py
RUN python3 ./manage.py collectstatic --noinput

COPY supervisor/prod.conf /etc/supervisor/conf.d/park-keeper.conf

CMD rm -rf /frontend/bower_components /frontend/dist /frontend/styles /frontend/static; \
    cd /opt/park-keeper/frontend; \
    test "$(ls /conf/config.coffee)" || cp src/app/config.coffee /conf/config.coffee; \
    rm src/app/config.coffee; \
    ln -s /conf/config.coffee src/app/config.coffee; \
    node_modules/.bin/gulp build; \
    cp -r bower_components /frontend/bower_components; \
    cp -r dist /frontend/dist; \
    cp -r styles /frontend/styles; \
    cd /opt/park-keeper/backend; \
    cp -r static /frontend/static; \
    test "$(ls /conf/settings.py)" || cp project/settings.sample.py /conf/settings.py; \
    rm project/settings.py; \
    ln -s /conf/settings.py project/settings.py; \
    python3 ./manage.py migrate; \
    /usr/bin/supervisord

