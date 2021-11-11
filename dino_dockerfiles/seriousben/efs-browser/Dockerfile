FROM alpine:3.6

RUN apk add --update nfs-utils

WORKDIR /efs
COPY mount.sh /

ENTRYPOINT [ "/mount.sh" ]
