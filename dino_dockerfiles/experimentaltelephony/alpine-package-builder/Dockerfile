FROM i386/alpine:3.6
RUN apk --update upgrade
RUN apk add --no-cache g++ musl-dev alpine-sdk coreutils cmake
RUN adduser -G abuild -g "Alpine package builder" -s /bin/sh -D builder
RUN echo "builder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN mkdir /packages
RUN chown builder:abuild /packages
COPY /abuilder /bin/
WORKDIR /home/builder/package
USER builder
ENTRYPOINT ["abuilder", "-r"]
ENV RSA_PRIVATE_KEY_NAME key.rsa
ENV PACKAGER_PRIVKEY /home/builder/${RSA_PRIVATE_KEY_NAME}
ENV REPODEST /packages
VOLUME ["/home/builder/package"]
