FROM sillelien/base-alpine:0.9.2
COPY build.sh /build.sh
RUN chmod 755 /build.sh
RUN /build.sh
COPY root /
RUN chmod 755 /bin/*.sh /scripts/fixes/*.sh /scripts/checks/*.sh
CMD s6-applyuidgid -u 999 -g 999 /bin/check.sh 2>&1 | logger
