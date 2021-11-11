FROM node:latest
MAINTAINER Mogria <m0gr14@gmail.com>

# install an ssh server and gosu
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y vim openssh-server && \
    curl -o /usr/bin/gosu -fsSL "https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-architecture)" && \
    chmod +x /usr/bin/gosu

ADD package.json /app/package.json
ADD bin/wetty.js /app/bin/wetty.js
ADD README.md /app/README.md
ADD .bowerrc /app/.bowerrc
ADD bower.json /app/bower.json
WORKDIR /app
# clone over git:// doesn't always work, rather use https://
RUN git config --global url."https://github.com".insteadOf "git://github.com" && \
    npm install --production && \
    npm install -g bower && \
    mkdir -p /app/public/vendor && \
    bower install --allow-root

ADD start-script.sh /usr/bin/start-script.sh
RUN echo 'export PATH="$PATH:/app/rts"' > /etc/profile.d/rts-path.sh && \
    groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv && \
    mkdir /rtshwetty && \
    useradd --uid 1338 rtshwetty --groups rtshplayers --home /rtshwetty && \
    chown rtshwetty:rtshwetty /rtshwetty && \
    chmod 700 /usr/bin/start-script.sh

ADD bin /app/bin
ADD public /app/public
ADD rts /app/rts/rts
ADD app.js /app/app.js
ADD LICENSE /app/LICENSE
ADD motd /etc/motd
ADD start-script.sh /app/start-script.sh

# for every command the client has add a symlink to rts here:
RUN ln -s /app/rts/rts /app/rts/cheat_create_unit && \
    ln -s /app/rts/rts /app/rts/move_unit && \
    ln -s /app/rts/rts /app/rts/build

RUN chown -R rtshwetty:rtshwetty /app && \
    find /app -type f -exec chmod -R 400 '{}' \; && \
    find /app -type d -exec chmod -R 500 '{}' \; && \
    chown -R rtshsrv:rtshsrv /app/rts && \
    chmod +x /app && \
    chmod +r /app && \
    chmod -R +x /app/rts && \
    chmod -R +r /app/rts


EXPOSE 3000

VOLUME ["/world", "/home", "/app/public"]

ENTRYPOINT ["start-script.sh"]
