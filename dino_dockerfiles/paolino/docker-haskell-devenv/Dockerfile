
## Dockerfile for a haskell environment
FROM       debian:stretch

MAINTAINER Paolo Veronelli <paolo.veronelli@gmail.com>

ENV LAST_UPDATED 2017-11-12

## ensure locale is set during build
ENV LANG            C.UTF-8
ENV HOME /root

#common
RUN apt-get update
RUN apt-get install -y ca-certificates g++ curl libgmp-dev
RUN apt-get install -y vim git wget tmux make gnupg

#stack
RUN curl -fSL \
        https://github.com/commercialhaskell/stack/releases/download/v1.6.0.20171022/stack-1.6.0.20171022-linux-x86_64-static.tar.gz\
        -o stack.tar.gz 
RUN curl -fSL \
       https://github.com/commercialhaskell/stack/releases/download/v1.6.0.20171022/stack-1.6.0.20171022-linux-x86_64-static.tar.gz.asc\ 
        -o stack.tar.gz.asc
RUN export GNUPGHOME="$(mktemp -d)"
RUN gpg --keyserver ha.pool.sks-keyservers.net \
	--recv-keys C5705533DA4F78D8664B5DC0575159689BEFB442 
RUN gpg --batch --verify stack.tar.gz.asc stack.tar.gz 
RUN tar -xf stack.tar.gz -C /usr/local/bin --strip-components=1 
RUN rm -rf "$GNUPGHOME" /var/lib/apt/lists/* /stack.tar.gz.asc /stack.tar.gz

ENV STACK_ROOT=/stack


RUN apt-get update && apt-get install -y sudo 




ENV PATH=$PATH:$HOME/.local/bin

env USER developer
RUN useradd $USER -s /bin/bash -m -u 1000 -G sudo 
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

env HOME /home/$USER
WORKDIR $HOME
USER $USER
RUN mkdir -p .vim/bundle
RUN mkdir -p .vim/undo

ADD bundles.vim bundles.vim

RUN curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
RUN vim -u bundles.vim +PlugInstall +qall

ADD bundles.vim .vimrc
ADD rest.vim rest.vim
RUN sudo chown -R $USER:$USER .
RUN cat rest.vim >> .vimrc
RUN rm bundles.vim rest.vim

WORKDIR $HOME/.vim/plugged/vimproc.vim
RUN make


WORKDIR $HOME
RUN sudo apt-get install -y busybox procps
RUN sudo apt-get install -y bzip2 xz-utils
RUN sudo apt-get install -y zlib1g-dev
RUN git clone https://github.com/reflex-frp/reflex-platform
RUN sudo apt-get install -y libtinfo-dev
RUN sudo apt-get install -y locales
Run sudo localedef -c -f UTF-8 -i en_US en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
RUN PATH=$HOME/.local/bin:$ATH
RUN curl https://nixos.org/nix/install | sh
RUN echo ". $HOME/.nix-profile/etc/profile.d/nix.sh" >>  $HOME/.bashrc
ADD hask.sh hask.sh
RUN cat hask.sh >> $HOME/.bashrc

ENTRYPOINT ["bash"]
