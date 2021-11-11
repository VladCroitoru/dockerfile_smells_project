FROM python:3.4

MAINTAINER 0.1 Daisuke NISHIMURA d@someonesgarden.org

RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
RUN export TERM=xterm

# BASIC INSTALLATION
RUN apt-get update  -y && apt-get clean
RUN apt-get install -y --force-yes vim gcc bzip2 sqlite3 openssl curl git wget tar && apt-get clean
RUN apt-get install -y --force-yes php5-common libapache2-mod-php5 php5-cli && apt-get clean

# FLASK, UWSGI, REDIS
RUN pip install Flask==0.10.1 uWSGI==2.0.8 requests==2.5.1 redis==2.10.3

# Cassandra python driver
RUN pip install cassandra-driver

####################################

RUN apt-get install -y --force-yes nodejs && apt-get clean
RUN apt-get install -y --force-yes npm && npm update -g npm && apt-get clean

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN export PATH=/usr/local/bin:$PATH
RUN alias envsudo="sudo env PATH=$PATH"

####################################

COPY . /home/uwsgi/

WORKDIR /home/uwsgi/app
RUN npm install && npm update
RUN npm install -g bower grunt-cli coffee-script && \
echo '{ "allow_root": true }' > /root/.bowerrc

WORKDIR /home/uwsgi/app/static
RUN bower install backbone underscore jquery  --save
RUN bower install bootstrap glyphicons glyphicons-halflings --save
RUN bower install angular angular-material angular-messages angular-route angular-resource angular-sanitize angular-local-storage --save


WORKDIR /home/uwsgi
USER uwsgi

EXPOSE 9090 9191 5000
CMD ["/home/uwsgi/cmd.sh"]