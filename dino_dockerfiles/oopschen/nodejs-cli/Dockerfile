# DocPad Dockerfile
FROM oopschen/alpine-nodejs:latest
MAINTAINER Ray Chen <linxray@gmail.com>

# Environments
ENV WORKDIR /mnt/nodejs

# install nodejs
WORKDIR ${WORKDIR}
VOLUME  ${WORKDIR}

CMD ["--help"]
ENTRYPOINT ["node"]
