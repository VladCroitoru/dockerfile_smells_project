FROM scratch
COPY bin /bin

ENV PORT 8080
ENV SSLPORT 8443

EXPOSE 8080 8443

ENV ADD_HEADERS='{"X-Real-Server": "echo-server"}'

WORKDIR /bin
ENTRYPOINT ["/bin/echo-server"]
