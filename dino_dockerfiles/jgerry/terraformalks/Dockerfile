FROM jenkins/jnlp-slave
MAINTAINER Jason Gerry

ENV TF_ALKS_PROVIDER_VERSION=1.0.0
ENV TERRAGRUNT_VERSION=v0.17.3
ENV PACKER_VERSION=1.3.3
ENV TERRAFORM_VERSION=0.11.10
ENV RUBY_VERSION=2.3.7
ENV JQ_VERSION=1.6

USER root

### add to sudoers
RUN usermod -aG sudo jenkins

### dev tools
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get -y update
RUN apt-get -y install apt-utils
RUN apt-get -y upgrade
RUN apt-get -y install build-essential readline-common libreadline-dev openssl libssl1.0-dev zlib1g-dev python-pip

### jq
RUN cd /usr/local/bin; curl -O https://github.com/stedolan/jq/releases/download/jq-${JQ_VERSION}/jq-linux64; mv jq-linux64 jq; chmod 755 jq

### alks
RUN wget -q -O tfalks.tar.gz https://github.com/Cox-Automotive/terraform-provider-alks/releases/download/${TF_ALKS_PROVIDER_VERSION}/terraform-provider-alks-linux-amd64.tar.gz && \
    tar -zxvf tfalks.tar.gz -C /usr/bin/ && \
    mv /usr/bin/terraform-provider-alks_* /usr/bin/terraform-provider-alks && \
    chmod a+x /usr/bin/terraform-provider-alks

### tfenv
RUN git clone https://github.com/kamatama41/tfenv.git /opt/.tfenv
RUN ln -s /opt/.tfenv/bin/tfenv /usr/local/bin/tfenv
RUN ln -s /opt/.tfenv/bin/terraform /usr/local/bin/terraform
RUN chown -R jenkins: /opt/.tfenv
COPY .terraformrc /home/jenkins/.terraformrc
RUN chown jenkins: /home/jenkins/.terraformrc

### packer
RUN wget https://releases.hashicorp.com/packer/${PACKER_VERSION}/packer_${PACKER_VERSION}_linux_amd64.zip
RUN unzip packer*
RUN mv packer /usr/local/bin

### terragrunt
ADD https://github.com/gruntwork-io/terragrunt/releases/download/${TERRAGRUNT_VERSION}/terragrunt_linux_amd64 /bin/terragrunt
RUN chmod +x /bin/terragrunt

### rbenv
RUN git clone https://github.com/rbenv/rbenv.git /home/jenkins/.rbenv
RUN git clone https://github.com/rbenv/ruby-build.git /home/jenkins/.rbenv/plugins/ruby-build
RUN chown -R jenkins: /home/jenkins/.rbenv
RUN ln -s /home/jenkins/.rbenv/bin/rbenv /usr/local/bin/rbenv

### set default shell for jenkins user to bash
RUN chsh -s /bin/bash jenkins

USER jenkins

RUN echo 'export PATH=$HOME/.rbenv/shims:$HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-build/bin:$PATH' >> ~/.bashrc
ENV PATH $HOME/.rbenv/shims:$HOME/.rbenv/bin:$HOME/.rbenv/plugins/ruby-build/bin:$PATH
RUN tfenv install $TERRAFORM_VERSION
RUN rbenv install $RUBY_VERSION
RUN rbenv global $RUBY_VERSION
RUN gem install terraform_landscape
RUN rbenv rehash

### aws cli
RUN pip install awscli --upgrade --user

ENTRYPOINT ["jenkins-slave"]
