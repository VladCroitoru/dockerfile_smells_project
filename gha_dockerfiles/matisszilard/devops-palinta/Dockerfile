FROM alpine:latest

ARG target
ADD ./build/linux-amd64/${target} /${target}

ARG target
ENV target_bin=$target
CMD ["sh", "-c", "/${target_bin}"]
