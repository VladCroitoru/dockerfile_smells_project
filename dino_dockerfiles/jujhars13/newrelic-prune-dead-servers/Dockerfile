FROM golang:1.2.2
MAINTAINER Jujhar Singh <jujhar@jujhar.com>

#get the project and setup
ADD prune-dead-servers.go /prune-dead-servers.go

#run our script (don't bother building just run interactivly)
ENTRYPOINT ["go","run","/prune-dead-servers.go"]

#DEFAULT params if --api-key not sent in
CMD ["--help"]
