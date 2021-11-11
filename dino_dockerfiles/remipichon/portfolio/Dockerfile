FROM alpine
MAINTAINER Remi P <pichon.remi.pr@gmail.com>

RUN apk update; apk --no-cache add dialog jq curl bash git;
COPY --chown=root data var
WORKDIR /var
ENTRYPOINT sh /var/portfolio.sh
