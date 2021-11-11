FROM atlassian/default-image:latest

# Download the necessary tools to deploy to kubernetes
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

# Install Azure CLI
RUN apt-get update && apt-get install -y libssl-dev libffi-dev python-dev python-pip
RUN curl -L https://aka.ms/InstallAzureCliBundled -o azure-cli_bundle.tar.gz
RUN tar -xvzf azure-cli_bundle.tar.gz
RUN azure-cli_bundle_*/installer
ENV PATH=$PATH:/root/bin

CMD ["/bin/bash"]
