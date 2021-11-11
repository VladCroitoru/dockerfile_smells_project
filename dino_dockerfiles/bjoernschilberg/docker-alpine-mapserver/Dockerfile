FROM alpine:3.9

LABEL maintainer="bjoern@intevation.de"
LABEL version="3.0"

RUN apk upgrade -U && \
    apk add libressl2.7-libcrypto --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main && \
    apk add mapserver --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
    apk add apache2

RUN mkdir -p /run/apache2

# Activate cgi modules.
RUN sed -i -e 's/#LoadModule\ cgid_module/LoadModule\ cgid_module/g' /etc/apache2/httpd.conf
RUN sed -i -e 's/#LoadModule\ cgi_module/LoadModule\ cgi_module/g' /etc/apache2/httpd.conf

# Write CustomLog output directly to /proc/self/fd/1 (which is STDOUT) and the ErrorLog to /proc/self/fd/2 (which is STDERR).
RUN sed -ri \
        -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
        -e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
        "/etc/apache2/httpd.conf"

# CORS on the server - enable cross-origin resource sharing
# https://enable-cors.org
RUN echo 'Header set Access-Control-Allow-Origin "*"' >> /etc/apache2/conf.d/default.conf

RUN cp /usr/bin/mapserv /var/www/localhost/cgi-bin/mapserv

# Use this to send MapServer’s debug messages to the Web server’s log file
# (i.e. “standard error”). If you are using Apache, your debug messages will be
# placed in the Apache error_log file.
# http://mapserver.org/de/optimization/debugging.html
ENV MS_ERRORFILE stderr

# http://mapserver.org/de/optimization/debugging.html#debug-levels
ENV MS_DEBUGLEVEL 5
ENV MAX_REQUESTS_PER_PROCESS 1000

EXPOSE 80

CMD ["/usr/sbin/httpd","-DFOREGROUND"]
