FROM oopschen/nodejs-cli:latest
MAINTAINER Ray Chen <linxray@gmail.com>

ENV WORKDIR /mnt/gulp-work
VOLUME ${WORKDIR}
WORKDIR ${WORKDIR}

RUN apk add -U git
RUN rm -rf /var/cache/apk/*

RUN npm install --global gulp-cli

CMD ["--version"]
ENTRYPOINT ["gulp"]
