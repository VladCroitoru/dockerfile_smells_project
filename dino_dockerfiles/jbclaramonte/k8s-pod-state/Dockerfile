FROM ubuntu

USER root

RUN apt-get update && apt-get install -y curl

COPY query-k8s.sh /

RUN chmod +x /query-k8s.sh

ENTRYPOINT /query-k8s.sh
