FROM alpine:3.7
WORKDIR /apex
ENV VERSION=0.8.1
RUN wget -O apex-install.sh 'https://up.apex.sh/install' && \
    export BINDIR=/usr/bin/ && \
    sh apex-install.sh $VERSION && \
    cd / && \
    rm -r /apex/ && \
    mkdir /work && \
    apk update && \
    apk add ca-certificates && \
    apk add git curl
WORKDIR /work
ADD entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
