FROM gliderlabs/alpine:3.1

MAINTAINER Mitch Dempsey <mitch@mitchdempsey.com>

RUN apk --update add \
    bash \
    curl \
    jq \
    sed \
    && ln -s /bin/sed /bin/gsed

COPY snapshot.sh /snapshot.sh

ENTRYPOINT ["/bin/bash"]

CMD ["/snapshot.sh"]
