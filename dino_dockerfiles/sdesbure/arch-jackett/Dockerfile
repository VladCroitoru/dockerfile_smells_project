FROM alpine:3.2
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>

WORKDIR /opt

# install dependencies
RUN apk add --update wget tar bzip2 curl-dev

#install mono
RUN apk add mono --update-cache --repository http://nl.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

# create group and user
RUN addgroup -S jackett
RUN adduser -s /bin/false -h /usr/share/Jackett -G jackett -S jackett
RUN mkdir -p /usr/share/Jackett
RUN chown -R jackett: /usr/share/Jackett

# grep Jackett
RUN wget --no-check-certificate https://github.com/Jackett/Jackett/releases/download/v0.6.45/Jackett.Binaries.Mono.tar.gz

# unpack and change owner
RUN tar -zxvf Jackett.Binaries.Mono.tar.gz
RUN chown -R jackett: /opt/Jackett

# map /config to host defined config path (used to store configuration from supervisor)
VOLUME /config

# map /opt/Jackett/.config/Jackett to host defined config path (used to store configuration from Jackett)
VOLUME /opt/Jackett/.config/Jackett

# expose port for http
EXPOSE 9117

# run
ENTRYPOINT ["/usr/bin/mono", "--debug", "/opt/Jackett/JackettConsole.exe"]
CMD ["-x", "true"]
