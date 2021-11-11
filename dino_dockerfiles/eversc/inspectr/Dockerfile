FROM ubuntu:16.10
RUN apt-get update && apt-get -y install ca-certificates
ADD main /main
ENTRYPOINT ["/main"]