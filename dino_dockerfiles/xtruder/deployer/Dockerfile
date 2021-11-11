FROM golang:alpine

RUN apk add --no-cache git

RUN git clone https://github.com/xtruder/terraform-provider-mysql.git $GOPATH/src/github.com/terraform-providers/terraform-provider-mysql
RUN go get github.com/terraform-providers/terraform-provider-mysql
RUN go install github.com/terraform-providers/terraform-provider-mysql

RUN git clone https://github.com/xtruder/terraform-provider-vault.git $GOPATH/src/github.com/terraform-providers/terraform-provider-vault
RUN go get github.com/terraform-providers/terraform-provider-vault
RUN go install github.com/terraform-providers/terraform-provider-vault

RUN git clone https://github.com/xtruder/terraform-provider-kubernetes.git $GOPATH/src/github.com/terraform-providers/terraform-provider-kubernetes
RUN go get github.com/terraform-providers/terraform-provider-kubernetes
RUN go install github.com/terraform-providers/terraform-provider-kubernetes

RUN git clone https://github.com/xtruder/terraform-provider-s3.git $GOPATH/src/github.com/negronjl/terraform-provider-s3
RUN go get github.com/negronjl/terraform-provider-s3
RUN go install github.com/negronjl/terraform-provider-s3

FROM hashicorp/terraform:0.11.8

WORKDIR /usr/local/deployer

ADD . /usr/local/deployer

COPY --from=0 /go/bin/terraform-provider-mysql resources/
COPY --from=0 /go/bin/terraform-provider-vault resources/
COPY --from=0 /go/bin/terraform-provider-kubernetes resources/
COPY --from=0 /go/bin/terraform-provider-s3 resources/

ENTRYPOINT src/loop.sh
