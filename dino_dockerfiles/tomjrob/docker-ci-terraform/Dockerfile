FROM alpine
MAINTAINER Tom Robinson (tomjrob@modhub.io)

RUN apk --update add git bash bzr git mercurial subversion openssh-client ca-certificates &&\
    rm -rf /var/cache/apk/*

ENV TERRAFORM_VERSION=0.6.12
ENV TERRAFORM_SHA256SUM=37513aba20f751705f8f98cd0518ebb6a4a9c2148453236b9a5c30074e2edd8d

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip &&\
    [ "${TERRAFORM_SHA256SUM}" = "$(sha256sum terraform_${TERRAFORM_VERSION}_linux_amd64.zip| awk '{print $1}')"  ] &&\
    unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /usr/bin/ &&\
    rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

CMD ["/usr/bin/terraform"]
