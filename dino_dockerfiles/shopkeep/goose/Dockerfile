# DOCKER-VERSION 0.11.1

#base the docker container off of a trusted golang image
FROM crosbymichael/golang

#install prerequisites
RUN apt-get update
RUN apt-get install -y gcc

#install goose
RUN go get 'bitbucket.org/liamstask/goose/cmd/goose'

#mount the app
RUN mkdir -p /opt/go/app/db
ADD ./dbconf.yml /opt/go/app/db/dbconf.yml
ONBUILD ADD ./migrations /opt/go/app/db/migrations

#set the working directory to /opt/go/app
WORKDIR /opt/go/app

#define go as the entrypoint
ENTRYPOINT ["/go/bin/goose", "--env=default"]
CMD ["up"]
