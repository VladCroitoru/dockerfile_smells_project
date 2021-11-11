FROM mwaeckerlin/very-base as build
RUN $PKG_INSTALL certbot
RUN mkdir /acme /etc/letsencrypt /var/log/letsencrypt
RUN $ALLOW_USER /acme /etc/letsencrypt /var/log/letsencrypt
RUN tar cp \
    /acme /etc/letsencrypt /var/log/letsencrypt /usr/lib/python* \
    $(which python3 certbot head tr) \
    $(for f in $(which python3) $(find /usr/lib/python* -name '*.so*'); do \
    ldd $f | sed -n 's,.* => \([^ ]*\) .*,\1,p'; \
    done 2> /dev/null) 2> /dev/null \
    | tar xpC /root/
RUN tar cp \
    $(find /root -type l ! -exec test -e {} \; -exec echo -n "{} " \; -exec readlink {} \; | sed 's,/root\(.*\)/[^/]* \(.*\),\1/\2,') 2> /dev/null \
    | tar xpC /root/
ADD renew.letsencrypt.sh /root/etc/periodic/daily/renew
ADD letsencrypt-config.sh /root/letsencrypt-config.sh
ADD letsencrypt-dns-authenticator.sh /root/letsencrypt-dns-authenticator.sh
ADD letsencrypt-dns-cleanup.sh /root/letsencrypt-dns-cleanup.sh
ADD letsencrypt-start.sh /root/letsencrypt-start.sh

FROM mwaeckerlin/cron as certbot
ENV CONTAINERNAME "letsencrypt"
ENV MODE "webroot"
ENV PREPEND "www"
VOLUME /etc/letsencrypt/live
COPY --from=build /root /
ENTRYPOINT [ "/letsencrypt-start.sh" ]