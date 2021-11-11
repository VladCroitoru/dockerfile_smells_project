FROM alpine:3.5
MAINTAINER Yann Weyer <yann.weyer@tu-berlin.de>

RUN mkdir -p /app
WORKDIR /app

RUN apk add --no-cache curl jq

COPY app/readinessProbe.sh k8s-readinessProbe
RUN ["chmod", "+x", "k8s-readinessProbe"]

ENTRYPOINT [ "/app/k8s-readinessProbe" ]