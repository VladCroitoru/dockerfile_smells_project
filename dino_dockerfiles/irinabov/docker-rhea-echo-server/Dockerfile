FROM fedora:latest
ENV NAME=docker-rhea-echo-server
LABEL maintainer="Irina Boverman <irina.boverman@gmail.com>" \
      summary="Docker image for rhea echo server" \
      name="irinabov/$NAME"
COPY ./build.sh /
RUN ./build.sh
WORKDIR node_modules/rhea/examples/websockets

EXPOSE 8888
ENTRYPOINT ["node", "echo.js"]
