FROM vizzbuzz/base-alpine:0.7
COPY at-3.1.16/ /tmp/at-3.1.16/
COPY build.sh /build.sh
RUN chmod 755 build.sh && apk upgrade && /build.sh
COPY etc/* /etc/
COPY bin/*.sh /bin/
COPY bin/httpd.sh /etc/services.d/httpd/run
COPY bin/cron.sh /etc/services.d/cron/run
RUN chmod 755 /etc/services.d/httpd/run /etc/services.d/cron/run /bin/*.sh

EXPOSE 8080