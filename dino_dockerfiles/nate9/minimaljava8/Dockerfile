FROM alpine:3.2
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories
RUN apk --update add openjdk8-jre@testing
CMD ["/usr/bin/java", "-version"]