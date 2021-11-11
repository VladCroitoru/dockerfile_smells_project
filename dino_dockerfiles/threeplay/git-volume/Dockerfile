FROM alpine:latest  
LABEL maintainer="eliran@threeplay.com"
LABEL base.name="Git Volume" \
      base.version="0.0.1"
RUN apk --no-cache add git
COPY entrypoint.sh /
ENTRYPOINT "/entrypoint.sh"

