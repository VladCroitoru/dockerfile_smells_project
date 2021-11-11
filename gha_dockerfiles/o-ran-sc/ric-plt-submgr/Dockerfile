#
#==================================================================================
#   Copyright (c) 2019 AT&T Intellectual Property.
#   Copyright (c) 2019 Nokia
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#==================================================================================
#
#
#	Abstract:	Builds a container to compile Subscription Manager's code
#	Date:		28 May 2019
#
###########################################################
#
###########################################################
FROM nexus3.o-ran-sc.org:10002/o-ran-sc/bldr-ubuntu18-c-go:1.9.0 as submgrcore

ARG g14="1.14.4"
ARG GOVERSION="1.14"
RUN wget -nv https://dl.google.com/go/go${g14}.linux-amd64.tar.gz \
     && tar -xf go${g14}.linux-amd64.tar.gz \
     && mv go /opt/go/${GOVERSION} \
     && rm -f go*.gz

ENV DEFAULTPATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV PATH=$DEFAULTPATH:/usr/local/go/bin:/opt/go/${GOVERSION}/bin:/root/go/bin

# Update CA certificates
RUN apt update && apt install --reinstall -y \
  ca-certificates \
  && \
  update-ca-certificates

RUN apt update && apt install -y iputils-ping net-tools curl tcpdump gdb valgrind

WORKDIR /tmp

#RUN git clone https://github.com/nokia/asn1c.git
#RUN cd asn1c && test -f configure || autoreconf -iv
#RUN cd asn1c &&  ./configure
#RUN cd asn1c && make
##RUN cd asn1c && make check
#RUN cd asn1c && make install

#
# Swagger
#
ARG SWAGGERVERSION=v0.23.0
ARG SWAGGERURL=https://github.com/go-swagger/go-swagger/releases/download/${SWAGGERVERSION}/swagger_linux_amd64
RUN wget --quiet ${SWAGGERURL} \
    && mv swagger_linux_amd64 swagger \
    && chmod +x swagger \
    && mv swagger /usr/local/bin/

#
# GO DELVE
#
RUN export GOBIN=/usr/local/bin/ ; \
    go get -u github.com/go-delve/delve/cmd/dlv \
    && go install github.com/go-delve/delve/cmd/dlv


#
# RMR
#
ARG RMRVERSION=4.7.4
ARG RMRLIBURL=https://packagecloud.io/o-ran-sc/release/packages/debian/stretch/rmr_${RMRVERSION}_amd64.deb/download.deb
ARG RMRDEVURL=https://packagecloud.io/o-ran-sc/release/packages/debian/stretch/rmr-dev_${RMRVERSION}_amd64.deb/download.deb
RUN wget --content-disposition ${RMRLIBURL} && dpkg -i rmr_${RMRVERSION}_amd64.deb
RUN wget --content-disposition ${RMRDEVURL} && dpkg -i rmr-dev_${RMRVERSION}_amd64.deb
RUN rm -f rmr_${RMRVERSION}_amd64.deb rmr-dev_${RMRVERSION}_amd64.deb


RUN mkdir /manifests/
RUN echo "rmrlib ${RMRVERSION} ${RMRLIBURL}" >> /manifests/versions.txt
RUN echo "rmrdev ${RMRVERSION} ${RMRDEVURL}" >> /manifests/versions.txt
RUN echo "swagger ${SWAGGERVERSION} ${SWAGGERURL}" >> /manifests/versions.txt


WORKDIR /opt/submgr

###########################################################
#
###########################################################
FROM submgrcore as submgre2apbuild


ENV CFLAGS="-DASN_DISABLE_OER_SUPPORT"
ENV CGO_CFLAGS="-DASN_DISABLE_OER_SUPPORT"

COPY 3rdparty 3rdparty
RUN cd 3rdparty/E2AP-v01.00.00 && \
    gcc -c ${CFLAGS} -I. -g -fPIC *.c  && \
    gcc *.o -g -shared -o libe2ap.so && \
    cp libe2ap.so /usr/local/lib/ && \
    cp *.h /usr/local/include/ && \
    ldconfig


RUN echo "E2AP         E2AP-v01.00.00" >> /manifests/versions.txt


COPY e2ap e2ap
RUN cd e2ap/libe2ap_wrapper && \
    gcc -c ${CFLAGS} -g -fPIC *.c  && \
    gcc *.o -g -shared -o libe2ap_wrapper.so && \
    cp libe2ap_wrapper.so /usr/local/lib/ && \
    cp *.h /usr/local/include/ && \
    ldconfig

# unittest
RUN cd e2ap && go test -v ./pkg/conv
RUN cd e2ap && go test -v ./pkg/e2ap_wrapper

# test formating (not important)
RUN cd e2ap && test -z "$(gofmt -l pkg/conv/*.go)"
RUN cd e2ap && test -z "$(gofmt -l pkg/e2ap_wrapper/*.go)"
RUN cd e2ap && test -z "$(gofmt -l pkg/e2ap/*.go)"
RUN cd e2ap && test -z "$(gofmt -l pkg/e2ap/e2ap_tests/*.go)"


###########################################################
#
###########################################################
FROM submgre2apbuild as submgrbuild
#
#
#
COPY go.mod go.mod
RUN go mod download

#
#
#
RUN mkdir pkg
COPY api api


ARG RTMGRVERSION=cd7867c8f527f46fd8702b0b8d6b380a8e134bea

RUN git clone "https://gerrit.o-ran-sc.org/r/ric-plt/rtmgr" \
    && git -C "rtmgr" checkout $RTMGRVERSION \
    && cp rtmgr/api/routing_manager.yaml api/ \
    && rm -rf rtmgr


RUN mkdir -p /root/go && \
    swagger generate client -f api/routing_manager.yaml -t pkg/ -m rtmgr_models -c rtmgr_client


RUN echo "rtmgrapi ${RTMGRVERSION} https://gerrit.o-ran-sc.org/r/ric-plt/rtmgr" >> /manifests/versions.txt

#
#
#
COPY pkg pkg
COPY cmd cmd

COPY go.sum go.sum
RUN go mod tidy

RUN mkdir -p /opt/bin && \
    go build -o /opt/bin/submgr cmd/submgr.go && \
    mkdir -p /opt/build/container/usr/local

RUN cp go.mod go.sum /manifests/
RUN grep gerrit /manifests/go.sum > /manifests/go_gerrit.sum


# unittest
COPY test/config-file.json test/config-file.json
ENV CFG_FILE=/opt/submgr/test/config-file.json
COPY test/uta_rtg.rt test/uta_rtg.rt
ENV RMR_SEED_RT=/opt/submgr/test/uta_rtg.rt 

#ENV CGO_LDFLAGS="-fsanitize=address"
#ENV CGO_CFLAGS="-fsanitize=address"

#
# To get debug from rmr
#
#RUN echo 5 >  /opt/submgr/level
#RUN RMR_VCTL_FILE=/opt/submgr/level go test -test.coverprofile /tmp/submgr_cover.out -count=1 -v ./pkg/control 

#
# go tests. comment out ipv6 localhost if exist when tests are executed.
#
RUN sed -r  "s/^(::1.*)/#\1/" /etc/hosts  > /etc/hosts.new \
    && cat /etc/hosts.new > /etc/hosts \
    && cat /etc/hosts  \
    && go test -failfast -test.coverprofile /tmp/submgr_cover.out -count=1 -v ./pkg/control \
    && go tool cover -html=/tmp/submgr_cover.out -o /tmp/submgr_cover.html    

# test formating (not important)
RUN test -z "$(gofmt -l pkg/control/*.go)"
RUN test -z "$(gofmt -l pkg/teststub/*.go)"
RUN test -z "$(gofmt -l pkg/teststubdummy/*.go)"
RUN test -z "$(gofmt -l pkg/teststube2ap/*.go)"


###########################################################
#
###########################################################
FROM ubuntu:18.04

RUN apt update && apt install -y iputils-ping net-tools curl tcpdump

COPY --from=submgrbuild /manifests /manifests
COPY --from=submgrbuild /opt/bin/submgr /
COPY --from=submgrbuild /usr/local/include/rmr /usr/local/include/
COPY --from=submgrbuild /usr/local/lib/librmr* /usr/local/lib/
COPY --from=submgrbuild /usr/local/lib/libe2ap* /usr/local/lib/
RUN ldconfig

COPY run_submgr.sh /
RUN chmod 755 /run_submgr.sh

#default config
COPY config /opt/config
ENV CFG_FILE=/opt/config/submgr-config.yaml
ENV RMR_SEED_RT=/opt/config/submgr-uta-rtg.rt

ENTRYPOINT ["/submgr"]
