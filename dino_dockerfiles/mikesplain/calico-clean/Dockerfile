FROM calico/ctl:v1.2.1
RUN apk --no-cache add \
      wget \
      bash \
      ca-certificates && \
      wget https://dl.k8s.io/v1.7.10/kubernetes-client-linux-amd64.tar.gz -O /tmp/k8s.tar.gz && \
      tar -zxvf /tmp/k8s.tar.gz && \
      rm -rf /tmp/k8s.tar.gz
COPY calico-clean.sh /calico-clean.sh

ENTRYPOINT /calico-clean.sh
