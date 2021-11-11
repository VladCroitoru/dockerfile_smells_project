FROM justckr/ubuntu-nginx-php:php7

MAINTAINER txt3rob
RUN apt-get update 
RUN apt-get install  curl wget debian-keyring -y
RUN apt-get update 
RUN apt-get install -y firefox
RUN apt-get install -y git libxrender-dev unzip libdbus-glib-1-2 locate nano xvfb  libasound2 libgeoip-dev libgtk2.0-0 bzip2 python supervisor 
RUN apt-get install -y x11-apps
RUN apt-get update && curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN wget https://download.slimerjs.org/releases/0.10.3/slimerjs-0.10.3.zip -O /tmp/slim.zip
RUN mkdir /home/slim/
RUN unzip /tmp/slim.zip -d /home/slim/
RUN mv /home/slim/slimerjs-0.10.3 /home/slim/slimerjs
RUN sed -i 's/MaxVersion=52/MaxVersion=89/g' /home/slim/slimerjs/application.ini
RUN chmod 755 /home/slim/slimerjs/slimerjs
RUN ln -s /home/slim/slimerjs/slimerjs /usr/bin/slimerjs
RUN chmod 755 /usr/bin/slimerjs
RUN export SLIMERJSLAUNCHER=/usr/bin/firefox
RUN rm /app/src/public/index.php
RUN rm /app/src/public/info.php


    
# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
	&& ln -sf /dev/stderr /var/log/nginx/error.log

EXPOSE 8080 1337 80
CMD ["service", "ssh", "start"]
CMD ["/bin/bash", "/start.sh"]


