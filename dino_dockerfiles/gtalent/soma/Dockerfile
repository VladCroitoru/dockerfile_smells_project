FROM debian:stretch

RUN apt-get update
RUN apt-get install -y apt-transport-https curl gnupg
RUN echo "deb https://deb.nodesource.com/node_6.x stretch main" >> /etc/apt/sources.list
RUN echo "deb-src https://deb.nodesource.com/node_6.x stretch main" >> /etc/apt/sources.list
RUN curl https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -

RUN apt-get update
RUN apt-get install -y python3-pip nodejs

###############################################################################
# Allow running without root

RUN curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture)" && \
    curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture).asc" && \
    chmod +x /usr/local/bin/gosu

# install Caddy
RUN curl -o caddy.tar.gz "https://caddyserver.com/download/linux/amd64?license=personal&telemetry=off"
RUN tar xf caddy.tar.gz caddy
RUN mv caddy /usr/local/bin/caddy
RUN rm caddy.tar.gz

ENV PYTHONUNBUFFERED 1

ENV SOMA_HOME /soma_home
RUN mkdir -p $SOMA_HOME /app/api_server
WORKDIR /app
# install requirements first, so unrelated changes
# don't require rerunning this part
ADD api_server/requirements.txt /app/api_server/
RUN apt-get install -y python3-cairocffi libpango1.0
RUN pip3 install -r api_server/requirements.txt
ADD api_server /app/api_server
ADD client /app/client

WORKDIR /app/client
RUN npm install
RUN npm run-script build

WORKDIR /app/api_server
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput

ADD docker/Caddyfile /app/

EXPOSE 2010
EXPOSE 2015

ADD docker/entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
