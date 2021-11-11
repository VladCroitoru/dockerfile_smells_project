FROM alpine

# Phase 1: DHCP server
RUN apk update && \
    apk add dhcp && \
    touch /var/lib/dhcp/dhcpd.leases
COPY conf/dhcpd.conf /etc/dhcp/dhcpd.conf

# Phase 2: PXE server
RUN apk update && \
    apk add tftp-hpa
# Don't add in the PXE files yet. That's OS-specific.

# Phase 3: Nginx and uwsgi servers
RUN apk update && \
    apk add python3 uwsgi-python3 uwsgi-cgi uwsgi nginx
COPY conf/nginx.conf /etc/nginx/nginx.conf
COPY conf/uwsgi_config.ini /etc/uwsgi_config.ini
COPY src/www /var/www
COPY src/cgi-bin /usr/lib/cgi-bin
COPY src/data /data
RUN mkdir /var/www/iso && \
    chown -R nginx:nginx /var/www && \
    rm -rf /var/www/localhost
# Creating testing database.
COPY src/tests.py /usr/lib/cgi-bin/tests.py
RUN cd /usr/lib/cgi-bin && python3 tests.py && rm tests.py

# Phase 4: Installing supervisord
RUN apk update && \
    apk add supervisor
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Phase 5: Finishing up.
RUN apk update && \
    apk add xorriso
# Declare volume at the end. Changes made after this will be discarded.
VOLUME ["/data"]
EXPOSE 80 69
CMD /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
