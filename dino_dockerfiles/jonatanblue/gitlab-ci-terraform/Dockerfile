FROM alpine:latest
MAINTAINER "Jonatan Bjork <jonatan@jonatanblue.se>"

ENV TERRAFORM_VERSION=0.10.8
ENV TERRAFORM_FILENAME=terraform_${TERRAFORM_VERSION}_linux_amd64.zip
ENV TERRAFORM_URL=https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/${TERRAFORM_FILENAME}
ENV TERRAFORM_SHA256SUM=b786c0cf936e24145fad632efd0fe48c831558cc9e43c071fffd93f35e3150db

RUN apk add --update git bash wget

RUN wget -q ${TERRAFORM_URL} \
  && echo "${TERRAFORM_SHA256SUM}  ${TERRAFORM_FILENAME}" | sha256sum -c
RUN unzip ${TERRAFORM_FILENAME} -d /bin
RUN rm -f ${TERRAFORM_FILENAME}
