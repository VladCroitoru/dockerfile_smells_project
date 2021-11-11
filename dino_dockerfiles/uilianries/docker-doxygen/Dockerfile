FROM alpine:3.7

LABEL maintainer="Uilian Ries <uilianries@gmail.com>"

RUN apk update && \
    apk add --no-cache -t .required_apks doxygen=1.8.13-r1 graphviz=2.40.1-r0

CMD ["/bin/ash"]
