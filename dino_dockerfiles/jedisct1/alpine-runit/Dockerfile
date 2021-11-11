FROM alpine:latest

ADD start_runit /sbin/
RUN 	mkdir /etc/container_environment &&\
        chmod a+x /sbin/start_runit && mkdir /etc/service && mkdir /etc/runit_init.d && \
        apk --no-cache --update upgrade && \
        apk add --no-cache bash util-linux coreutils findutils grep runit

CMD ["/sbin/start_runit"]
