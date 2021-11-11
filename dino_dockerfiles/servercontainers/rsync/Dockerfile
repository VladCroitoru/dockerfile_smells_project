FROM alpine

ENV PATH="/container/scripts:${PATH}"

RUN export rsync_version=3.2.3 \
 \
 && apk add --no-cache alpine-sdk \
                       bash \
                       openssl-dev \
                       lz4-dev \
                       zstd-dev \
                       xxhash-dev \
 \
 && wget https://www.samba.org/ftp/rsync/src/rsync-${rsync_version}.tar.gz \
 && tar xvf rsync-${rsync_version}.tar.gz \
 && rm rsync-${rsync_version}.tar.gz \
 && cd rsync-${rsync_version} \
 \
 && ./configure --prefix=/ \
 && make \
 && make install \
 \
 && cd - \
 && rm -rf rsync-${rsync_version} \
 \
 && apk del alpine-sdk \
 \
 && touch /etc/rsyncd.secrets \
 && chmod 600 /etc/rsyncd.secrets

VOLUME ["/shares"]

EXPOSE 873

COPY . /container/
RUN cp /container/config/rsyncd.conf /etc/rsyncd.conf

HEALTHCHECK CMD ["docker-healthcheck.sh"]
ENTRYPOINT ["entrypoint.sh"]

CMD [ "rsync", "--no-detach", "--daemon", "--config", "/etc/rsyncd.conf" ]
