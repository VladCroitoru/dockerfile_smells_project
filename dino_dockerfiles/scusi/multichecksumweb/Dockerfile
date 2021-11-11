# busybox is our base image
FROM busybox 
# maintainer
MAINTAINER Florian Walther <flw@posteo.de>

# copy Md5Webserver binary into docker image
# binary can be builded from source with:
#  CGO_ENABLED=0 GOOS=linux go build -a -tags netgo -ldflags '-w' .
#
ADD MultiChecksumWeb /MultiChecksumWeb
# add templates to docker image
ADD tmpl /tmpl

# set entrypoint for docker image
# This is the app we gonna start when the image is started
ENTRYPOINT /MultiChecksumWeb

# set environment variable 'PORT' used by Md5Webserver binary as port to bind to.
ENV PORT 80

# expose port 80 to the outside world from the docker image
EXPOSE 80
