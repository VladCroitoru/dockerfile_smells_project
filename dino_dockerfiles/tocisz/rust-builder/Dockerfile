FROM rust:latest

ADD build.sh /

WORKDIR /usr/src/myapp
VOLUME ["/usr/src/myapp"]
VOLUME ["/installed"]

ENV name hello
CMD sh /build.sh $name
