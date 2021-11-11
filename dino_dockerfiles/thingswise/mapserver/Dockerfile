FROM python:2.7.12

RUN apt-get update && apt-get -y install mapserver-bin lighttpd && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY lighttpd.conf /lighttpd.conf

VOLUME /map

ENV DOC_ROOT "/"
ENV PORT 5000
ENV DEBUG 0
ENV MIN_PROCS 1
ENV MAX_PROCS 3
ENV MAX_LOAD_PER_PROC 4
ENV IDLE_TIMEOUT 20

EXPOSE $PORT

CMD ["lighttpd", "-D", "-f", "/lighttpd.conf"]
