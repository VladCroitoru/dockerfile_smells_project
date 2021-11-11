FROM alpine:3.4

ARG vcs_ref="Unknown"
ARG vcs_branch="Unknown"
ARG build_date="Unknown"

ENV DEHYDRATED_VERSION v0.4.0
ENV GOPATH /go
VOLUME /var/dehydrated

RUN apk add --update bash curl openssl ca-certificates jq git go make python py-pip
RUN pip install awscli
RUN	mkdir -p /var/dehydrated/certs ;\
	mkdir -p /var/dehydrated/accounts

# Install cli53
RUN go get github.com/barnybug/cli53 ;\
    cd $GOPATH/src/github.com/barnybug/cli53 ;\
    make build ;\
    chmod a+x cli53 ;\
    ln -s $GOPATH/src/github.com/barnybug/cli53/cli53 /bin/cli53 ;\
    rm -rf /var/cache/apk/*

# Install route53 hook
COPY route53hook.sh /opt/route53hook.sh
RUN chmod a+x /opt/route53hook.sh

WORKDIR /opt

# Install dehydrated
ADD https://github.com/lukas2511/dehydrated/archive/${DEHYDRATED_VERSION}.tar.gz /opt/dehydrated.tar.gz
COPY config /opt/config
RUN tar -zxf dehydrated.tar.gz

ENTRYPOINT ["/opt/dehydrated-0.4.0/dehydrated", "--accept-terms"]

LABEL org.label-schema.vcs-ref=$vcs_ref \
      org.label-schema.vcs-branch=$vcs_branch \
	  org.label-schema.build-date=$build_date \
	  maintainer="jose@armesto.net"
