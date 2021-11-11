FROM nginx

COPY ./binaries/distributor-linux-amd64 /bin/distributor
COPY ./config.template /etc/distributor/config.template

WORKDIR /etc/distributor

CMD distributor > /etc/nginx/nginx.conf && nginx
