FROM golang:1.16 as builder
WORKDIR /webhook
COPY ./ /webhook
RUN go env -w GOPROXY=https://goproxy.cn,direct && ./build.sh

FROM debian:latest as webhook
WORKDIR /workspace
COPY --from=builder /webhook/build/webhook .
COPY --from=builder /webhook/build/config/ config/
CMD cd /workspace && ./webhook


