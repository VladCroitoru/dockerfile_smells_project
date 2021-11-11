FROM debian:buster-slim
RUN apt update
RUN apt install -y curl wget nano python3 openssh-server php net-tools
WORKDIR /
EXPOSE 80
EXPOSE 22
RUN rm -rf /var/www/html/index.html
COPY files/index.php /var/www/html/index.php
COPY files/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chmod 4755 /bin/bash

