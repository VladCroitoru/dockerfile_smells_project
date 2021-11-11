FROM alpine
RUN apk update && apk add build-base fuse-dev
COPY fuse-tutorial-2016-03-25 fuse-tutorial-2016-03-25/
COPY bbfs.sh /usr/local/bin
RUN cd fuse-tutorial-2016-03-25 && ./configure && make && cp src/bbfs /usr/local/bin && mkdir -p /src /dest
ENTRYPOINT ["bbfs.sh"]
