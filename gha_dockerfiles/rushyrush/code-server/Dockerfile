FROM codercom/code-server:3.12.0

RUN sudo apt-get update \
 && sudo apt-get install -y unzip

# Install terraform
COPY --from=hashicorp/terraform:1.0.8 /bin/terraform /bin/
RUN terraform version

# Install awscli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
  && unzip -qq awscliv2.zip \
  && sudo ./aws/install \
  && rm -rf ./awscliv2.zip ./aws
RUN aws --version

# Install kubectl
RUN sudo apt-get update \
  && sudo apt-get install -y apt-transport-https ca-certificates curl \
  && sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg \
  && echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list \
  && sudo apt-get update \
  && sudo apt-get install -y kubectl
RUN kubectl version --client

# install helm
RUN curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | sudo bash
RUN helm version

# fluxcli install
RUN curl -s https://fluxcd.io/install.sh | sudo bash
RUN flux --version