FROM alpine:latest

RUN apk add --no-cache bash jq python py-pip curl

RUN pip install --upgrade pip && pip install awscli

RUN cd /usr/local/bin/ && \
      curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
      chmod +x /usr/local/bin/kubectl

ADD ./k8s-aws-routes-kubenet.sh /k8s-aws-routes-kubenet.sh

RUN chmod +x /k8s-aws-routes-kubenet.sh

ENV K8S_AWS_ROUTES_INTERVAL=30

CMD while true; do /k8s-aws-routes-kubenet.sh --yes; sleep $K8S_AWS_ROUTES_INTERVAL; done
