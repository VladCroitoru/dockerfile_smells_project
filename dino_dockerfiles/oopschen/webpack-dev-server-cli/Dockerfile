FROM oopschen/nodejs-cli:latest
MAINTAINER Ray Chen <linxray@gmail.com>

ENV WORKDIR /mnt/webpack-work
VOLUME ${WORKDIR}
WORKDIR ${WORKDIR}

EXPOSE 3000
EXPOSE 5000
EXPOSE 8080
EXPOSE 8081

STOPSIGNAL SIGKILL

RUN npm install --global webpack-dev-server
CMD ["--help"]
ENTRYPOINT ["webpack-dev-server"]
