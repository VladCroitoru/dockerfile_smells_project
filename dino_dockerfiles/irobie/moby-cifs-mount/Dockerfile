FROM alpine
MAINTAINER Robert Crandall <robert.crandall@gmail.com>

# forked from https://github.com/vipconsult/dockerfiles/tree/master/moby-nfs-mount
# we need nsenter to enter the docker host and mount a global cifs mount so all ocntainers can use it for persistant data
# install nsenter so we can enter the docker host - this is the only way with the current moby linux
RUN apk update && apk add util-linux
ADD start.sh /start.sh
RUN chmod o+x /start.sh

CMD ["/start.sh"]
