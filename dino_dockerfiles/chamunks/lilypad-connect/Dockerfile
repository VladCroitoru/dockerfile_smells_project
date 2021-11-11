##########################
## Alpine based OPENSSH ##
##########################
FROM frolvlad/alpine-oraclejdk8
MAINTAINER Chamunks <Chamunks@gmail.com>

RUN mkdir -p /app
ADD http://ci.lilypadmc.com/job/Go-Server-Connect/lastSuccessfulBuild/artifact/target/connect-linux-amd64 /app/connect-linux-amd64
RUN chmod +x /app/connect-linux-amd64

EXPOSE 5091
WORKDIR /app/
ENTRYPOINT  ["/app/connect-linux-amd64"]
