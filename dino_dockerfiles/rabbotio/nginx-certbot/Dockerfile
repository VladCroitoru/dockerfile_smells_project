FROM alpine

# Nginx's config
RUN mkdir -p /etc/nginx/conf.d
COPY etc/nginx/conf.d /etc/nginx/conf.d

# Script
COPY usr/local/bin/dhparam.sh /usr/local/bin/dhparam.sh
COPY usr/local/bin/new.sh /usr/local/bin/new.sh
COPY usr/local/bin/entrypoint.sh /usr/local/bin/entrypoint.sh

# Excutable
RUN chmod u+x /usr/local/bin/dhparam.sh
RUN chmod u+x /usr/local/bin/new.sh
RUN chmod u+x /usr/local/bin/entrypoint.sh

# Renewal
COPY etc/cron.daily/renew.sh /etc/cron.daily/renew.sh
RUN chmod u+x /etc/cron.daily/renew.sh

WORKDIR /usr/local/bin

# Entry
ENTRYPOINT [ "entrypoint.sh" ]
