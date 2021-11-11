FROM python:3-alpine
MAINTAINER azunyuuuuuuu

# environment variables
ENV HENKAKU_HOST "192.168.1.100"
ENV HENKAKU_STAGE2_PORT "4000"
ENV HENKAKU_PKG_PORT "8888"

# expose ports
EXPOSE 8888 4000

# add tools
RUN apk add --no-cache git go

# add files
WORKDIR /app
RUN ["git", "clone", "https://github.com/henkaku/henkaku.git", "/app"]
ADD run.sh /app/run.sh

# prepare files
RUN chmod +x run.sh
RUN ./build.sh http://${HENKAKU_HOST}:${HENKAKU_STAGE2_PORT}/ http://${HENKAKU_HOST}:${HENKAKU_PKG_PORT}/pkg

CMD ["/bin/sh", "/app/run.sh"]