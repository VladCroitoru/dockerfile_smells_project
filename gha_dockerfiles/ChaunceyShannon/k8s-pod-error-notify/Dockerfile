#FROM gcr.io/distroless/static:nonroot
FROM ubuntu:20.04

# USER nonroot:nonroot

# https://github.com/GoogleContainerTools/distroless
# 这个最小基础镜像有ssl的证书, 所以不需要安装
RUN mkdir -p /app;\
  apt update; \
  apt install -y ca-certificates

WORKDIR /app

COPY k8s-pod-error-notify /bin/k8s-pod-error-notify

# CMD ["/bin/k8s-pod-error-notify", "-c", "/app/k8s-pod-error-notify.ini"]
CMD ["/bin/k8s-pod-error-notify"]
