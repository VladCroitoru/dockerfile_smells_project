FROM nginx:1.11.10

COPY default.conf /etc/nginx/conf.d/default.conf
COPY bin/entry.sh /usr/local/bin/

RUN chmod 744 /usr/local/bin/entry.sh && \
    chown root:root /usr/local/bin/entry.sh

CMD /usr/local/bin/entry.sh
