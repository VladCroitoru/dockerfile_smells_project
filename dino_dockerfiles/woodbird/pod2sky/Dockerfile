FROM alpine:latest
MAINTAINER MarcoXu<woodbird456@gmail.com>
ADD jq /usr/local/bin/
ADD pod2sky.sh /usr/local/bin
ADD schedulePod2sky.sh /usr/local/bin
RUN apk update && apk add curl && apk add bash
ENTRYPOINT schedulePod2sky.sh
