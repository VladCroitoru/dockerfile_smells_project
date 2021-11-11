FROM busybox:ubuntu-14.04

RUN mkdir -p /opt
ADD ./k8s-endpoint-updater /opt/k8s-endpoint-updater

ENTRYPOINT ["/opt/k8s-endpoint-updater"]
