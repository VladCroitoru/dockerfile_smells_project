FROM xorcode/nodejs
RUN \
  add-apt-repository -y ppa:nginx/stable && \
  DEBIAN_FRONTEND="noninteractive" apt-get update && \
  DEBIAN_FRONTEND="noninteractive" apt-get -y install nginx && \
  npm install harp -g && mkdir /srv/www && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY default /etc/nginx/sites-available/default
COPY nginx.conf /etc/nginx/nginx.conf
