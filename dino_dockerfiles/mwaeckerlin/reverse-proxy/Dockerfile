FROM mwaeckerlin/very-base as certbot
RUN $PKG_INSTALL certbot
RUN mkdir /acme /etc/letsencrypt /var/log/letsencrypt
RUN $ALLOW_USER /acme /etc/letsencrypt /var/log/letsencrypt
RUN tar cp \
    /acme /etc/letsencrypt /var/log/letsencrypt /usr/lib/python* \
    $(which python3 certbot) \
    $(for f in $(which python3) $(find /usr/lib/python* -name '*.so*'); do \
    ldd $f | sed -n 's,.* => \([^ ]*\) .*,\1,p'; \
    done 2> /dev/null) 2> /dev/null \
    | tar xpC /root/
RUN tar cp \
    $(find /root -type l ! -exec test -e {} \; -exec echo -n "{} " \; -exec readlink {} \; | sed 's,/root\(.*\)/[^/]* \(.*\),\1/\2,') 2> /dev/null \
    | tar xpC /root/

FROM mwaeckerlin/letsencrypt as letsencrypt

FROM mwaeckerlin/very-base AS tools
RUN $PKG_INSTALL inotify-tools openssl
RUN mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
RUN $ALLOW_USER /etc/nginx
RUN tar cp \
    /etc/nginx/sites-available /etc/nginx/sites-enabled  \
    /bin /tmp \
    $(find /usr/bin -type l) \
    $(which openssl) \
    $(which inotifywait) \
    $(which getent) \
    $(for f in $(which openssl) $(which inotifywait); do \
    ldd $f | sed -n 's,.* => \([^ ]*\) .*,\1,p'; \
    done 2> /dev/null) 2> /dev/null \
    | tar xpC /root/
RUN tar cp \
    $(find /root -type l ! -exec test -e {} \; -exec echo -n "{} " \; -exec readlink {} \; | sed 's,/root\(.*\)/[^/]* \(.*\),\1/\2,') 2> /dev/null \
    | tar xpC /root/

FROM mwaeckerlin/nginx AS nginx

FROM mwaeckerlin/scratch AS assemble
COPY --from=certbot /root /
COPY --from=letsencrypt /letsencrypt-config.sh /letsencrypt-config.sh
COPY --from=tools /root /
COPY --from=nginx / /
ADD proxy.conf /etc/nginx/proxy.conf
ADD default.conf /etc/nginx/conf.d/default.conf
ADD start.sh /start.sh
ADD nginx-configure.sh /nginx-configure.sh
USER root
RUN sed -i '/^daemon/d' /etc/nginx/nginx.conf

FROM mwaeckerlin/scratch
ENV CONTAINERNAME "reverse-proxy"
ENV DEBUG_LEVEL "error"
ENV BASIC_AUTH_REALM ""
ENV HTTP_PORT "8080"
ENV HTTPS_PORT "8443"
EXPOSE ${HTTP_PORT} ${HTTPS_PORT}
VOLUME /etc/nginx/sites-available
VOLUME /etc/nginx/sites-enabled
VOLUME /etc/nginx/basic-auth
VOLUME /etc/letsencrypt
VOLUME /acme
COPY --from=assemble / /
CMD /start.sh
HEALTHCHECK --interval=10s --timeout=5s --start-period=60s --retries=3 \
    CMD /bin/sh -c "netstat -tln | grep -q \"0\.0\.0\.0:\${HTTP_PORT}\""
