FROM mrobson/fuse-base-install:6.2.1.84

MAINTAINER Matthew Robson <matthewrobson@gmail.com>

USER 1000

EXPOSE 8181 1099

WORKDIR /opt/fuse/${FUSE_ARTIFACT}

ENTRYPOINT ["/opt/fuse/jboss-fuse-full/bin/fuse"]

CMD ["server"]
