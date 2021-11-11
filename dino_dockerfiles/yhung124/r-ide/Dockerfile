# For persional ide

FROM ubuntu:16.04
MAINTAINER Raymond, yhung124@gmail.com

ENV HOME /home/build
ENV PATH "$PATH:$HOME/bin:/usr/sbin"

# Install essential packages
COPY sources.list /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y sudo vim-nox-py2 git make gawk libncurses5-dev wget python unzip patch ack-grep tree man ctags bash-completion && \
    rm -rf /var/lib/apt/lists/*

RUN addgroup --gid 233 docker
RUN adduser --disabled-password --gecos "" -shell /bin/bash --home /home/build --uid 500 build && \
    echo "build:os1234" | chpasswd && \
    usermod -a -G sudo,docker build && \
    echo "build ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    mkdir -p /home/build/bin

COPY bashrc /home/build/bashrc
RUN cat /home/build/bashrc >> /home/build/.bashrc && rm /home/build/bashrc

ADD https://raw.githubusercontent.com/git/git/f483a0aa2a4ca30f4fa76ea4aff621e59cdb882c/contrib/completion/git-completion.bash /home/build/.git-completion.bash
ADD https://raw.githubusercontent.com/git/git/be099661f41e661eac8af2b4879a84a9eb9a7b9b/contrib/completion/git-prompt.sh /home/build/.git-prompt.sh
ADD https://raw.githubusercontent.com/moby/moby/1.12.x/contrib/completion/bash/docker /etc/bash_completion.d/docker
RUN chmod 644 /etc/bash_completion.d/docker
ADD https://storage.googleapis.com/kubernetes-release/release/v1.5.7/bin/linux/amd64/kubectl /home/build/bin/kubectl
RUN chmod 755 /home/build/bin/kubectl

USER build
WORKDIR /home/build

RUN git config --global push.default matching
RUN git config --global diff.tool vimdiff
RUN git config --global difftool.prompt false
RUN git config --global alias.d difftool
RUN git config --global alias.st status
RUN git config --global alias.ci commit
RUN git config --global alias.co checkout
RUN git config --global user.email "yhung124@gmail.com"
RUN git config --global user.name "Raymond"

RUN wget https://github.com/wting/autojump/archive/release-v22.5.0.tar.gz
RUN tar -zxvf release-v22.5.0.tar.gz
RUN cd ./autojump-release-v22.5.0 && ./install.py -f && cd ..
RUN rm -rf ./autojump-release-v22.5.0 && rm ./release-v22.5.0.tar.gz

# VIM configure
COPY vimrc.vundle /home/build/.vimrc
COPY vimrc /home/build/vimrc
USER root
RUN chown -R build:build /home/build/
USER build
RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
RUN vim +PluginInstall +qall
RUN cat /home/build/vimrc >> /home/build/.vimrc && rm -rf /home/build/vimrc
