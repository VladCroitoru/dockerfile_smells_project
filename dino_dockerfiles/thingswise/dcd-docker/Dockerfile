FROM progrium/busybox
MAINTAINER Alexander Lukichev

ADD http://gocfs.s3-website-us-east-1.amazonaws.com/dcd /dcd
RUN chmod +x /dcd

CMD ["/dcd"]
