# this is a multi-stage Dockerfile; image dependencies look something like this:
#  bot --v
#        +--> install --> final
#  web --^

### webapp stage
FROM node:8 AS web
WORKDIR /build
ENV NPM_CONFIG_LOGLEVEL warn
RUN apt-get update && apt-get install -y build-essential && \
    mkdir -p web/build && \
    npm -v

# cached npm environments
COPY ./web/package.json /build/web/
COPY ./web/package.json /build/web/build/
RUN cd /build/web && \
    npm install && \
    cd build && \
    npm install --production

# web content
COPY ./web web
COPY ./Makefile Makefile
RUN make web



### bot stage
FROM debian:8 AS bot
WORKDIR /build

# system prereqs
RUN apt-get update && \
    apt-get install -y build-essential cmake curl git musl-tools && \
    mkdir -p bot/contest-exec
ENV PATH=/root/.cargo/bin:$PATH

# get us some rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain stable -y && \
    rustup target add x86_64-unknown-linux-musl

# see https://github.com/thehydroimpulse/nanomsg.rs/blob/master/Makefile
RUN git clone -b 1.0.0 --depth 1 https://github.com/nanomsg/nanomsg.git nanomsg-1.0.0 && \
    (cd nanomsg-1.0.0 && mkdir build && cd build && cmake .. && cmake --build .) && \
    (cd nanomsg-1.0.0/build && cmake --build . --target install)

# cached cargo environments
COPY ./bot/Cargo.* bot/
COPY ./bot/contest-exec/Cargo.* bot/contest-exec/
RUN cd bot && \
    cargo fetch && \
    cd contest-exec && \
    cargo fetch

# build bot & helper
COPY ./bot bot
COPY ./Makefile Makefile
RUN make bot contest-exec



### installation stage
FROM debian:8 AS install
WORKDIR /build
RUN apt-get update && apt-get install -y build-essential rsync
COPY ./Makefile Makefile
COPY --from=web /build/web web
COPY --from=bot /build/bot bot
RUN make install



### final image
FROM node:8-alpine
CMD ["/opt/progcon/bin/progcon-server"]
VOLUME /opt/progcon/conf /opt/progcon-problems /opt/progcon/logs
RUN apk add --no-cache diffutils openjdk8 && \
    ln -s /usr/lib/jvm/default-jvm/bin/javac /usr/bin/javac

COPY --from=install /opt /opt/
RUN chmod 4755 /opt/progcon/bin/contest-exec

USER 1000
