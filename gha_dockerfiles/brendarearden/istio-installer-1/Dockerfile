FROM alpine:latest

ENV ISTIO_VERSION 1.6.1

RUN apk update && apk add curl bash coreutils
RUN curl -L https://istio.io/downloadIstio | sh -
RUN mv istio-${ISTIO_VERSION}/bin/istioctl /usr/bin && chmod +x /usr/bin/istioctl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl
COPY scripts /usr/local/app/scripts/
RUN chmod +x /usr/local/app/scripts/init_kubeconfig.sh /usr/local/app/scripts/run.sh /usr/local/app/scripts/create_istio_system.sh
ENTRYPOINT [ "/usr/local/app/scripts/run.sh" ]