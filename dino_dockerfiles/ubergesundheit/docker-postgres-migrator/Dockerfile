FROM alpine

RUN apk add --update bash curl postgresql-client && rm -rf /var/cache/apk/*

RUN curl -L https://raw.githubusercontent.com/naquad/shmig/a06917d0ecf3e198c4416e4f6caa8580b73e0f97/shmig > /usr/local/bin/shmig \
  && chmod u+x /usr/local/bin/shmig

COPY migrate.sh /usr/local/bin/

ENTRYPOINT ["migrate.sh"]

CMD ["up"]
