FROM alpine

# use curl to get certificate verification
RUN apk add --no-cache curl

RUN curl -sL https://dl.k8s.io/v1.20.1/kubernetes-client-linux-amd64.tar.gz \
    | tar -xz -C /usr --strip-components=2

WORKDIR /workspace

RUN chmod a+rwx /workspace

ENV HOME=/workspace

ENTRYPOINT ["/usr/bin/kubectl"]
