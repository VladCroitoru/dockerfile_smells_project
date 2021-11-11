FROM alpine

ENV KUBE_VERSION="1.19.6/2021-01-05"
ENV HELM_VERSION="v3.5.4"
ENV AWS_IAM_AUTHENTICATOR_VERSION="1.19.6/2021-01-05"

RUN apk add --update --no-cache ca-certificates bash git curl gettext tar gzip python3 py-pip jq \
 && pip3 install awscli yq --upgrade \
 && curl -L https://amazon-eks.s3.us-west-2.amazonaws.com/${KUBE_VERSION}/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
 && curl -L https://amazon-eks.s3-us-west-2.amazonaws.com/${AWS_IAM_AUTHENTICATOR_VERSION}/bin/linux/amd64/aws-iam-authenticator -o /usr/local/bin/aws-iam-authenticator \
 && curl -L https://get.helm.sh/helm-${HELM_VERSION}-linux-amd64.tar.gz | tar xz && mv linux-amd64/helm /usr/local/bin/helm && rm -rf linux-amd64 \
 && chmod +x /usr/local/bin/kubectl /usr/local/bin/aws-iam-authenticator /usr/local/bin/helm \
 && helm plugin install https://github.com/chartmuseum/helm-push

ADD update_images.sh *.yml /
RUN chmod +x /update_images.sh

