# USE ALPINE LINUX
FROM alpine
RUN apk update
# INSTALL BASIC DEV TOOLS, GHC, GMP & ZLIB
RUN echo "https://s3-us-west-2.amazonaws.com/alpine-ghc/8.0" >> /etc/apk/repositories
ADD https://raw.githubusercontent.com/mitchty/alpine-ghc/master/mitch.tishmack%40gmail.com-55881c97.rsa.pub \
    /etc/apk/keys/mitch.tishmack@gmail.com-55881c97.rsa.pub
RUN apk update
RUN apk add alpine-sdk git ca-certificates ghc gmp-dev zlib-dev
# GRAB A RECENT BINARY OF STACK
RUN curl -L https://www.stackage.org/stack/linux-x86_64-static | tar xz --wildcards --strip-components=1 -C /usr/local/bin '*/stack'

# COMPRESS WITH UPX
ADD https://github.com/lalyos/docker-upx/releases/download/v3.91/upx /usr/local/bin/upx
RUN chmod 755 /usr/local/bin/upx
