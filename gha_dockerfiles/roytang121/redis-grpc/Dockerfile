FROM alpine:latest

WORKDIR /root/
RUN apk update
RUN apk add curl
RUN apk add alpine-sdk
RUN apk add protoc

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

COPY . ./
RUN ~/.cargo/bin/cargo build --release

FROM alpine:latest
WORKDIR /root/
COPY --from=0 /root/target/release/redis-grpc /root/redis-grpc
ENTRYPOINT ["/root/redis-grpc"]