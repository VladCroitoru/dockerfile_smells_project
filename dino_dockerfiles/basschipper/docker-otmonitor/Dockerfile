FROM frolvlad/alpine-glibc:alpine-3.13

RUN mkdir /app && mkdir /data \
  && /usr/bin/wget http://otgw.tclcode.com/download/otmonitor-x64 -O /app/otmonitor \
  && chmod +x /app/otmonitor

CMD ["/app/otmonitor", "--daemon", "-f", "/data/otmonitor.conf"]
