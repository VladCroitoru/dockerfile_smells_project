FROM ubuntu:16.04
MAINTAINER Ryan Meharg <ryan.meharg@altoros.com>

# Setup
ENV GOVERSION 1.8.1
ENV GOPATH $HOME/go
ENV GOBIN $HOME/go/bin
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$HOME/bin:/usr/local/go/bin:$GOBIN

RUN mkdir -p ~/bin
RUN mkdir -p $GOBIN

# Install common packages
RUN cat /etc/apt/sources.list | sed 's/archive/us.archive/g' > /tmp/s && mv /tmp/s /etc/apt/sources.list
RUN apt-get update && apt-get -y --no-install-recommends install wget curl
RUN apt-get -y --no-install-recommends install ruby libroot-bindings-ruby-dev \
           build-essential git ssh zip software-properties-common dnsutils \
           iputils-ping traceroute jq vim wget unzip sudo iperf screen tmux \
           file openstack tcpdump nmap less s3cmd s3curl direnv \
           netcat npm nodejs-legacy python3-pip python3-setuptools \
           apt-utils libdap-bin mysql-client mongodb-clients postgresql-client-9.5 \
           redis-tools libpython2.7-dev libxml2-dev libxslt-dev

# Insall python
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python2.7 ./get-pip.py && rm -f python2.7 ./get-pip.py
RUN pip3 install --upgrade pip

# Install Google Cloud SDK
RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-xenial main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN apt-get update && sudo apt-get -y --no-install-recommends install google-cloud-sdk

# Install AWS CLI
RUN pip3 install awscli

# Install Azure CLI 
# RUN npm install -g azure-cli

# Install CF CLI
RUN curl -L \
    "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" \
    | tar -C /usr/local/bin -zx

# Install vault
RUN wget $(wget -O- -q https://www.vaultproject.io/downloads.html | grep linux_amd | awk -F "\"" '{print$2}') -O vault.zip && unzip vault.zip && cp vault /usr/local/bin/vault
RUN chmod 755 /usr/local/bin/vault

# Install safe
RUN cd /usr/local/bin && wget -q -O safe \
    "$(curl -s https://api.github.com/repos/starkandwayne/safe/releases/latest \
    |jq --raw-output '.assets[] | .browser_download_url' | grep linux)" && chmod +x safe

# Install credhub
RUN cd /usr/local/bin && wget -q -O - https://github.com/cloudfoundry-incubator/credhub-cli/releases/download/1.2.0/credhub-linux-1.2.0.tgz | tar xzf - > credhub && chmod 0755 credhub

# Install terraform
RUN cd /usr/local/bin/ && curl -o terraform.zip \
    "https://releases.hashicorp.com/terraform/0.9.11/terraform_0.9.11_linux_amd64.zip" \
    && unzip terraform.zip && rm -f terraform.zip

# Install cf-uaac
RUN gem install cf-uaac --no-rdoc --no-ri

# Install fly (Concourse CLI)
RUN cd /usr/local/bin && wget -q -O fly \
    "$(curl -s https://api.github.com/repos/concourse/fly/releases/latest \
    |jq --raw-output '.assets[] | .browser_download_url' | grep linux)" && chmod +x fly

# Install BOSH v2 CLI
RUN cd /usr/local/bin && wget -q -O bosh https://s3.amazonaws.com/bosh-cli-artifacts/bosh-cli-2.0.45-linux-amd64 && chmod 0755 bosh && ln -s bosh bosh2

# Install bosh-bootloader
RUN cd /usr/local/bin && wget -q -O bbl \
    "$(curl -s https://api.github.com/repos/cloudfoundry/bosh-bootloader/releases/latest \
    |jq --raw-output '.assets[] | .browser_download_url' | grep linux)" && chmod +x bbl 

# Install spiff
RUN cd /usr/local/bin && wget -q -O spiff https://github.com/cloudfoundry-incubator/spiff/releases/download/v1.0.8/spiff_linux_amd64.zip \
    && chmod +x spiff

# Install spruce
RUN cd /usr/local/bin && wget -q -O spruce \
    "$(curl -s https://api.github.com/repos/geofffranks/spruce/releases/latest \
    |jq --raw-output '.assets[] | .browser_download_url' | grep linux | grep -v zip)" && chmod +x spruce

# Install asg-creator
RUN cd /usr/local/bin && wget -q -O asg-creator \
    "$(curl -s https://api.github.com/repos/cloudfoundry-incubator/asg-creator/releases/latest \
    |jq --raw-output '.assets[] | .browser_download_url' | grep linux | grep -v zip)" && chmod +x asg-creator

# Install genesis
RUN curl "https://raw.githubusercontent.com/starkandwayne/genesis/master/bin/genesis" > /usr/bin/genesis \
    && chmod 0755 /usr/bin/genesis

# Install kubectl
RUN cd /usr/local/bin && \
    curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod 0755 kubectl

# Install bucc
RUN mkdir -p .bucc && git clone https://github.com/starkandwayne/bucc.git && \
    ln -s $HOME/.bucc/bucc/bin/bucc /usr/local/bin/bucc

# Install Go
RUN wget -q -O - "https://storage.googleapis.com/golang/go${GOVERSION}.linux-amd64.tar.gz" \
    | sudo tar -C /usr/local -zx
RUN sudo add-apt-repository -y ppa:masterminds/glide
RUN sudo apt-get update && sudo apt-get -y --no-install-recommends install glide

## -------------
## Pivotal Tools
## -------------
## Install Pivotal OM
#RUN cd /usr/local/bin && wget -q -O om \
#    "$(curl -s https://api.github.com/repos/pivotal-cf/om/releases/latest \
#    |jq --raw-output '.assets[] | .browser_download_url' | grep linux)" && chmod +x om 
#
## Install Pivnet CLI
#RUN cd /usr/local/bin && wget -q -O pivnet \
#    "$(curl -s https://api.github.com/repos/pivotal-cf/pivnet-cli/releases/latest \
#    |jq --raw-output '.assets[] | .browser_download_url' | grep linux | grep -v zip)" && chmod +x pivnet
#
## Install Pivotal CF Ops
#RUN cd /usr/local/bin && wget -q -O cfops \
#    "$(curl -s https://api.github.com/repos/pivotalservices/cfops/releases/latest \
#    |jq --raw-output '.assets[] | .browser_download_url')" && chmod +x cfops

# Cleanup
RUN apt-get -y autoremove && apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/log/*

CMD ["/bin/bash"]
