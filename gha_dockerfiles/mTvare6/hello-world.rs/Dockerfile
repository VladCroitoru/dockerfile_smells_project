FROM rust:1.31

MAINTAINER 'mTvare6' <https://github.com/mTvare6/hello-world.rs>

LABEL maintainer="mTvare6"

LABEL memory_safe=true

WORKDIR /usr/src/hello-world
COPY . .

RUN cargo install --path .

ENTRYPOINT ["hello-world"]

