ARG REGISTRY=quay.io/parkside-securities
FROM $REGISTRY/docker-parkside-runtime:master-68

ENV GOROOT /usr/local/go
ENV GOPATH /root/go
ENV GIT_SUBREPO_ROOT /root/repos/git-subrepo
ENV PATH /root/repos/git-subrepo/lib:/usr/local/go/bin:/root/go/bin:${PATH}
ENV MANPATH /root/repos/git-subrepo/man:$MANPATH
RUN mv /etc/apt/sources.list.d/nodesource.list /etc/apt/sources.list.d/nodesource.list.disabled

RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list && \
    apt-get update -yq && apt-get upgrade -yq && \
    apt-get install -yq git netcat rsync zsh libgd-dev fontconfig \
    libcairo2-dev libpango1.0-dev libgts-dev graphviz \
    emacs silversearcher-ag \
    kubectl less zlib1g-dev libffi-dev libssl-dev vim-nox tmate libxss1 \
    build-essential plantuml jq iproute2 && \
    apt-get clean
RUN curl -sfL https://direnv.net/install.sh | bash
RUN curl -s "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    rm -rf awscli-bundle*
RUN wget -q https://dl.google.com/go/go1.11.11.linux-amd64.tar.gz && \
    tar -xvf go1.11.11.linux-amd64.tar.gz && \
    mv go /usr/local && \
    rm go1.11.11.linux-amd64.tar.gz
RUN curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.12.7/2019-03-27/bin/linux/amd64/aws-iam-authenticator && \
    chmod +x ./aws-iam-authenticator && \
    mv ./aws-iam-authenticator /usr/local/bin/
RUN curl -s -LO https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv3.3.0/kustomize_v3.3.0_linux_amd64.tar.gz && \
    tar xzf kustomize_v3.3.0_linux_amd64.tar.gz && \
    mv kustomize /usr/local/bin/kustomize && \
    rm kustomize_v3.3.0_linux_amd64.tar.gz && \
    chmod a+x /usr/local/bin/kustomize
RUN curl -sL https://graphviz.gitlab.io/pub/graphviz/stable/SOURCES/graphviz.tar.gz -O && \
    tar xvfp graphviz.tar.gz && \
    cd  graphviz-* && \
    ./configure && make && make install && \
    cd - && rm -rf graphviz*

ENV REDIS_VERSION=6.2.1
RUN curl -OL https://download.redis.io/releases/redis-${REDIS_VERSION}.tar.gz && \
    tar xzf redis-${REDIS_VERSION}.tar.gz && \
    cd redis-${REDIS_VERSION} && \
    make install && \
    cp ./src/redis-server /usr/local/bin/ && \
    cp ./src/redis-benchmark /usr/local/bin/ && \
    cp ./src/redis-sentinel /usr/local/bin/ && \
    cp ./src/redis-cli /usr/local/bin/ && \
    chmod +x /usr/local/bin/redis-* && \
    rm -rf /tmp/redis-${REDIS_VERSION}

RUN wget -q https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein && \
    chmod +x lein && \
    mv lein /usr/local/bin && \
    lein -v
RUN mkdir -p /root/repos && \
    git clone https://github.com/ingydotnet/git-subrepo /root/repos/git-subrepo && \
    git clone https://github.com/awslabs/git-secrets.git /root/repos/git-secrets && \
    git clone https://github.com/magicmonty/bash-git-prompt.git /root/.bash-git-prompt --depth=1 && \
    git clone https://github.com/olivierverdier/zsh-git-prompt.git /root/.zsh-git-prompt && \
    git clone https://github.com/jonmosco/kube-ps1.git /root/.kube-ps1 && \
    git clone https://github.com/ahmetb/kubectx /root/repos/kubectx && \
    chmod +x /root/repos/kubectx/kubectx && \
    chmod +x /root/repos/kubectx/kubens && \
    ln -s /root/repos/kubectx/kubectx /usr/local/bin/kubectx && \
    ln -s /root/repos/kubectx/kubens /usr/local/bin/kubens && \
    cd /root/repos/git-secrets && make install && cd - && \
    curl -OL https://github.com/eraserhd/rep/releases/download/v0.1.2/rep-0.1.2-linux-amd64.tar.gz && \
    tar zxvfp rep-0.1.2-linux-amd64.tar.gz && \
    cp rep-0.1.2-linux-amd64/rep /usr/local/bin/rep && chmod a+x /usr/local/bin/rep && \
    cp rep-0.1.2-linux-amd64/rep.1 /usr/local/man/rep.1 && \
    rm -rf rep-0.1.2-linux-amd64 && \
    npm install -g shadow-cljs
RUN pip install mkdocs && \
    pip install plantuml-markdown && \
    pip install markdown-include && \
    pip install mkdocs-rtd-dropdown
RUN python -m venv /usr/local/dbt-env && \
    . /usr/local/dbt-env/bin/activate && \
    python -m pip install -U pip && \
    pip install wheel && \
    pip install dbt
RUN curl -L https://github.com/drone/drone-cli/releases/download/v1.2.0/drone_linux_amd64.tar.gz | tar zx && \
    mv drone /usr/local/bin/
RUN curl -sL https://raw.githubusercontent.com/babashka/babashka/master/install > bb-install && \
    chmod +x bb-install && \
    ./bb-install
COPY entrypoint.sh /usr/local/bin
COPY gitignore_global /root/gitignore_global
COPY gitconfig /root/.gitconfig
COPY bashrc /root/.bashrc
COPY zshrc /root/.zshrc
WORKDIR /parkside
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
