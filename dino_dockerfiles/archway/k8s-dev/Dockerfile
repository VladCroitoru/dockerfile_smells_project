FROM ubuntu:latest

ENV KUBECTL_VERSION 1.9.0
ENV HELM_VERSION 2.8.0
ENV HELM_FILENAME helm-v${HELM_VERSION}-linux-amd64.tar.gz
ENV DOTNET_VERSION 2.1.4
ENV GOLANG_VERSION 1.10

# install base apps
RUN apt-get update && apt install -y sudo git openssh-client openssh-server gnupg curl make vim bash 

# setup ssh server
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo >> /etc/ssh/sshd_config
RUN echo 'X11UseLocalhost no' >> /etc/ssh/sshd_config

# install and setup Kubernetes client
RUN set -ex \
    && curl -LO https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/amd64/kubectl \
    && chmod +x ./kubectl \
    && mv ./kubectl /usr/local/bin/kubectl

RUN set -ex \
    && curl -sSL https://storage.googleapis.com/kubernetes-helm/${HELM_FILENAME} | tar xz \
    && mv linux-amd64/helm /usr/local/bin/helm \
    && rm -rf linux-amd64

RUN helm init --client-only

# install X11 and GTK.
RUN apt-get update && apt-get install -y libgtk2.0-0 libgconf2-4 \
    libnss3 libasound2 libxtst6 libcanberra-gtk-module libgl1-mesa-glx libxss1 xauth \
    apt-transport-https fonts-takao

# install Visual Studio code
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg &&\
    mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg &&\
    sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'

RUN apt-get update && apt-get install -y code

# add user for develop
RUN useradd -ms /bin/bash me
RUN echo 'root:1qaz2wsx' | chpasswd
RUN echo 'me:1qaz2wsx' | chpasswd
RUN sh -c "echo 'me       ALL=(ALL) ALL' >> /etc/sudoers"
WORKDIR /home/me

# install .NET Core SDK
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main" > /etc/apt/sources.list.d/dotnetdev.list'
RUN apt-get update && apt-get install -y dotnet-sdk-${DOTNET_VERSION}

# install Open JDK 8
RUN apt-get update &&\
    apt-get -y install openjdk-8-jdk &&\
    sh -c "echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >> /etc/profile.d/jdk.sh" &&\
    sh -c "echo 'export PATH=\$JAVA_HOME/bin:\$PATH' >> /etc/profile.d/jdk.sh" &&\
    . /etc/profile.d/jdk.sh

# install GO language
RUN curl -s https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-amd64.tar.gz | tar -C /usr/local -xz
ENV PATH $PATH:/usr/local/go/bin

# install Node.JS
RUN apt-get update &&\
    apt-get install -y nodejs npm &&\
    npm cache clean &&\
    npm install n -g &&\
    n stable &&\
    ln -sf /usr/local/bin/node /usr/bin/node &&\
    apt-get purge -y nodejs npm

RUN apt-get clean all

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

USER me
RUN code --install-extension ms-vscode.csharp
RUN code --install-extension vscjava.vscode-java-pack

RUN mkdir $HOME/go
RUN sh -c "echo 'export GOPATH=$HOME/go' >> .bashrc" &&\
    sh -c "echo 'export PATH=$PATH:$GOPATH/bin' >> .bashrc"
RUN code --install-extension lukehoban.go

USER root

