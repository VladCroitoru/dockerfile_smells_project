FROM golang

RUN go get github.com/calavera/docker-volume-glusterfs

EXPOSE 7878

ENTRYPOINT ["docker-volume-glusterfs"]

CMD ["-help"]
