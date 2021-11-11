FROM tianon/speedtest

RUN apk add --update gnuplot && rm -rf /var/cache/apk/*

ADD cmd.sh /

ADD speedtest.gnu /

ADD data/ /data

VOLUME /data

CMD ["/cmd.sh"]
