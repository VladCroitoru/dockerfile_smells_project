FROM node:boron

ENV DEBIAN_FRONTEND noninteractive

WORKDIR /opt/current-app

ADD . .

# "allow_root"  is needed for bower to work properly

RUN apt-get update -y && \
        apt-get install -y \
        python-pip \
        python2.7 \
        python2.7-dev \
        nginx && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    npm install && \
    echo '{ "allow_root": true }' > /root/.bowerrc && \
    npm run bower_install && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    dpkg -l|grep python3| awk '{ print $2 }'| xargs apt purge -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ADD nginx/dashboards.conf /etc/nginx/sites-available/default

ENTRYPOINT [ "/opt/current-app/start" ]

EXPOSE 80
