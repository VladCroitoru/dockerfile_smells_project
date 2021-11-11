FROM ubuntu:16.04

ARG DOCKER_GID
ARG USER_ID=1000
ARG USER_NAME=dev

ENV GO_VERSION 1.9.3.linux-amd64
ENV KUBECTL_VERSION 1.9.0
ENV ISTIO_VERSION 0.5.1
ENV TERM xterm-256color
ENV USER_ID=${USER_ID}
ENV USER_NAME=${USER_NAME}

RUN apt-get update 
RUN apt-get install -y vim \
        software-properties-common \
        wget \
        curl \
        libcurl4-openssl-dev \
        zsh \
        dos2unix \
        build-essential \
        git \
        apt-file \
        python-dev \
        python-pip \
        python3-dev \
        python3-pip \
        apt-transport-https \
        ca-certificates \
        man \
        unzip \
        ctags \
        locales \
        sudo \
        gnupg2 \
        libevent-dev \
        pkg-config \
        libncurses5-dev \
        automake \
        openjdk-8-jdk

RUN apt-file update

RUN git clone https://github.com/tmux/tmux.git /tmp/tmux && \
      cd /tmp/tmux && \
      sh autogen.sh && \
      ./configure && \
      make && \
      make install && \
      rm -rf /tmp/tmux

RUN curl -LO http://invisible-island.net/datafiles/current/terminfo.src.gz && \
      gunzip terminfo.src.gz && \
      tic -x terminfo.src

RUN rm /etc/localtime && \
        ln -s /usr/share/zoneinfo/America/New_York /etc/localtime && \
        localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8

ENV LANG en_US.utf8

RUN curl -L https://github.com/docker/compose/releases/download/1.19.0-rc2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && \
	chmod +x /usr/local/bin/docker-compose

RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

RUN add-apt-repository ppa:ansible/ansible && \
	add-apt-repository ppa:neovim-ppa/stable && \
        add-apt-repository ppa:brightbox/ruby-ng && \
        add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) \
        stable" && \
        apt-get update && \ 
        apt-get install -y neovim docker-ce ansible ruby-switch ruby2.2 ruby2.2-dev && \
        rm -rf /var/lib/apt/lists/*

RUN useradd --shell /bin/bash -u $USER_ID -o -c "" -m $USER_NAME&& \
      echo "${USER_NAME}:${USER_NAME}" | chpasswd
ENV HOME /home/$USER_NAME
RUN mkdir -p /home/$USER_NAME/bin
WORKDIR /home/$USER_NAME
RUN mkdir -p /home/$USER_NAME/.local/share/nvim/shada && \
        touch /home/$USER_NAME/.local/share/nvim/shada/main.shada && \
        chmod -R 775 /home/$USER_NAME/.local


RUN chown -R "${USER_NAME}":"${USER_NAME}" /home/"${USER_NAME}"
RUN chown -R "${USER_NAME}":"${USER_NAME}" /home/"${USER_NAME}"/bin

USER $USER_NAME
RUN git clone https://github.com/tomgeorge/oh-my-zsh.git ~/.oh-my-zsh && \
        git clone https://github.com/tomgeorge/dotfiles && \
        git clone https://github.com/tomgeorge/vimfiles /home/$USER_NAME/.vim && \
        cd dotfiles && \
        git pull origin master && \
        ./links.sh

RUN pip3 install neovim --user && \
        nvim -E -s -c "source ~/.config/nvim/init.vim" -c PluginInstall -c qa -V || true && \
        nvim -E -s -c "source ~/.config/nvim/init.vim" -c UpdateRemotePlugins -c qa -V || true
RUN pip3 install awscli  --user
USER root

VOLUME /var/shared

RUN gem install neovim
RUN usermod -aG docker dev && \
      usermod -aG sudo dev && \
      usermod -aG daemon dev
RUN find . -type d -exec chmod 775 {} \;
RUN chsh dev -s "$(which zsh)"

ADD https://dl.google.com/go/go$GO_VERSION.tar.gz /usr/local
RUN cd /usr/local && \
           tar -xf go$GO_VERSION.tar.gz && \
           rm go$GO_VERSION.tar.gz && \
           mkdir -p /home/$USER_NAME/go \
            /home/$USER_NAME/bin \
            /home/$USER_NAME/lib \
            /home/$USER_NAME/include \
            /var/shared  && \
            touch /var/shared/placeholder && \
            ln -s /var/shared/.ssh

ENV PATH /home/$USER_NAME/bin:/usr/local/go/bin:$PATH
ENV LD_LIBRARY_PATH /home/$USER_NAME/lib:$LD_LIBRARY_PATH

RUN wget https://releases.hashicorp.com/terraform/0.11.2/terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482 && unzip terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482 -d /usr/local/bin && rm terraform_0.11.2_linux_amd64.zip?_ga=2.104669568.1844800320.1517421482-308538760.1517421482

RUN wget https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip && \
        unzip packer_1.2.3_linux_amd64.zip -d /usr/local/bin

RUN wget https://storage.googleapis.com/kubernetes-release/release/v$KUBECTL_VERSION/bin/linux/amd64/kubectl && \
      chmod +x kubectl && \
      mv kubectl /usr/local/bin

RUN wget https://github.com/istio/istio/releases/download/0.5.1/istio-$ISTIO_VERSION-linux.tar.gz && \
        tar -xf istio-$ISTIO_VERSION-linux.tar.gz && \
        mv istio-$ISTIO_VERSION/bin/istioctl /usr/local/bin && \
        chmod +x /usr/local/bin/istioctl && \
        rm -rf istio-$ISTIO_VERSION

USER dev
ENTRYPOINT ["/usr/bin/zsh"]
