FROM circleci/node:10 as base

# set up terraform
FROM base AS tf
WORKDIR /home/circleci
RUN export TF_VERSION="0.12.31" \
  && curl https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip -o terraform_${TF_VERSION}_linux_amd64.zip \
  && unzip terraform_${TF_VERSION}_linux_amd64.zip -d terraform

# copy tf from intermediate layer
FROM base AS final
WORKDIR /usr/bin
COPY --from=tf /home/circleci/terraform .
# ensure binary exists
RUN ls /usr/bin/terraform

ENV HELM_VERSION="v2.17.0"

RUN export CLOUD_SDK_REPO="cloud-sdk-jessie" \
  && echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
  && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add - \
  && sudo apt-get update \
  && sudo apt-get upgrade -y \
  && sudo apt-get install -y google-cloud-sdk kubectl gawk \
  && sudo apt-get -y autoclean \
  && sudo curl -L https://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -o helm.tar.gz \
  && sudo tar -xzO linux-amd64/helm -f helm.tar.gz > ~/helm \
  && sudo mv ~/helm /usr/local/bin/helm \
  && sudo chmod +x /usr/local/bin/helm \
  && helm init --client-only

WORKDIR /home/circleci
