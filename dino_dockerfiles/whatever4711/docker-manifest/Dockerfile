FROM alpine
RUN apk --no-cache --update upgrade \
 && apk --no-cache add ca-certificates curl \
 && curl -o /usr/bin/docker https://6582-88013053-gh.circle-artifacts.com/1/work/build/docker-linux-amd64 \
 && chmod +x /usr/bin/docker \
 && apk del curl
ENTRYPOINT ["/usr/bin/docker", "-D", "manifest"]
CMD ["--help"]
