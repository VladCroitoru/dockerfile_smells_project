# Ubuntu 14.04, Go 1.3, Discussie (from source)
#
# Example command:
#  sudo docker run -v /tmp:/data -P --net=host discussie/discussie
#
FROM schmichael/ubuntu-go:v14.04-1.3.0
MAINTAINER Michael Schurter <m@schmichael.com>
VOLUME ["/data"]
EXPOSE 8000
ADD . /opt/go/src/github.com/discussie/discussie
RUN cd /opt/go/src/github.com/discussie/discussie && go get ./...
CMD ["-bind=:8000", "-db=/data/discussied.sqlite3", "-site=/opt/go/src/github.com/discussie/discussie/public"]
ENTRYPOINT ["discussied"]
