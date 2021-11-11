FROM registry.access.redhat.com/ubi8/ubi
MAINTAINER sig-platform@spinnaker.io
LABEL name='clouddriver'
LABEL maintainer='info@opsmx.io'
LABEL release=1
LABEL version='1.20.3'
LABEL summary='Red Hat certified Open Enterprise Spinnaker ubi8 container image for clouddriver'
LABEL description='Certified Open Enterprise Spinnaker is an Enterprise grade, Red Hat certified and OpsMx supported release of the popular and critically acclaimed Continuous Delivery platform Spinnaker'
LABEL vendor='OpsMx'
COPY clouddriver-web/build/install/clouddriver /opt/clouddriver

ENV KUBECTL_VERSION v1.16.0

RUN yum -y install bash unzip wget unzip java-11-openjdk-headless.x86_64 python2 && \
  wget -nv https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.zip && \
  unzip -qq google-cloud-sdk.zip -d /opt && \
  rm google-cloud-sdk.zip && \
  CLOUDSDK_PYTHON="python2.7" /opt/google-cloud-sdk/install.sh --usage-reporting=false --bash-completion=false --additional-components app-engine-java app-engine-go && \
  rm -rf ~/.config/gcloud

RUN wget https://storage.googleapis.com/kubernetes-release/release/${KUBECTL_VERSION}/bin/linux/amd64/kubectl && \
  chmod +x kubectl && \
  mv ./kubectl /usr/local/bin/kubectl

RUN wget https://amazon-eks.s3-us-west-2.amazonaws.com/1.13.7/2019-06-11/bin/linux/amd64/aws-iam-authenticator && \
  chmod +x ./aws-iam-authenticator && \
  mv ./aws-iam-authenticator /usr/local/bin/aws-iam-authenticator && \
  ln -sf /usr/local/bin/aws-iam-authenticator /usr/local/bin/heptio-authenticator-aws

RUN yum -y install python2-pip && \
  pip2 install --upgrade awscli==1.16.258 s3cmd==2.0.1 python-magic && \
  yum -y remove python2-pip && \
  yum clean all

ENV PATH "$PATH:/usr/local/bin/"

ENV PATH=$PATH:/opt/google-cloud-sdk/bin/

RUN adduser spinnaker

RUN mkdir -p /opt/clouddriver/plugins

USER spinnaker

CMD ["/opt/clouddriver/bin/clouddriver"]
