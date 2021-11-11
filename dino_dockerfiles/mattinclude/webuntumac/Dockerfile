FROM ubuntu:14.04

MAINTAINER Matthew A. Brassey version: 0.1

ENV DEBIAN_FRONTEND noninteractive

ADD initialize/startup.sh /startup.sh

RUN apt-get update && apt-get install -y apache2 supervisor npm \
    git x11vnc wget python python-numpy unzip atop xvfb firefox openbox vim feh nano menu terminator tmux

RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN npm install pm2 -g
RUN pm2 update
RUN pm2 install pm2-webshell
RUN pm2 set pm2-webshell:username ubuntu
RUN pm2 set pm2-webshell:password webuntumac
RUN sed -i -e 's/#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc
RUN echo 'cat /etc/motd && echo " "' >> /root/.bashrc
RUN cd /root && git clone https://github.com/kanaka/noVNC.git && \
    cd noVNC/utils && git clone https://github.com/kanaka/websockify websockify && \
    cd /root && \
    chmod 0755 /startup.sh && \
    apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*
RUN wget \
  https://github.com/joewalnes/websocketd/releases/download/v0.2.10/websocketd-0.2.10-linux_amd64.zip && \
  unzip websocketd-0.2.10-linux_amd64.zip -d . && \
  mv websocketd /usr/local/bin && \
  rm -f websocketd-0.2.10-linux_amd64.zip

RUN git clone https://github.com/joewalnes/web-vmstats.git /var/www/web-vmstats

COPY initialize/pm2.style.css /root/.pm2/node_modules/pm2-webshell/node_modules/tty.js/static/style.css
COPY initialize/index.tty /root/.pm2/node_modules/pm2-webshell/node_modules/tty.js/static/index.html
COPY initialize/user.css /root/.pm2/node_modules/pm2-webshell/node_modules/tty.js/static/user.css
COPY initialize/user.js /root/.pm2/node_modules/pm2-webshell/node_modules/tty.js/static/user.js
COPY initialize/000-default.conf /etc/apache2/sites-enabled/000-default.conf
COPY initialize/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY initialize/config.py /usr/share/terminator/terminatorlib/config.py
COPY initialize/initialize.htm /var/www/index.html
COPY initialize/.htaccess /var/www/.htaccess
COPY initialize/tmux.conf /root/.tmux.conf
COPY initialize/.bashrc /root/.bashrc
COPY initialize/motd /etc/motd.tail

COPY launch /var/www/launch

EXPOSE 80 8010 369
CMD ["/usr/bin/supervisord"]
