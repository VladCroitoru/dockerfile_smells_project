FROM golang:1.9

WORKDIR /tmp/oc

ENV OC_PACKAGE_NAME=openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit
RUN    mkdir -p /tmp/oc && cd /tmp/oc \
    && wget -q -O oc.tar.gz https://github.com/openshift/origin/releases/download/v3.6.0/$OC_PACKAGE_NAME.tar.gz \
    && tar -zxvf oc.tar.gz $OC_PACKAGE_NAME/oc \
    && cp $OC_PACKAGE_NAME/oc /usr/bin/oc \
    && rm -rf /tmp/oc

WORKDIR /go/src/github.com/ninech/actuator
COPY . ./

RUN    go-wrapper download \
    && go-wrapper install github.com/ninech/actuator \
    && mkdir /actuator \
    && cp /go/src/github.com/ninech/actuator/actuator.yml /actuator/ \
    && rm -rf /go/src

WORKDIR /actuator

USER 10000
EXPOSE 8080
CMD ["/go/bin/actuator"]
