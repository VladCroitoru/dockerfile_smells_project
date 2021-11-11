FROM ubuntu:14.04

###########
# system
###########

RUN adduser --disabled-password --gecos "" ubuntu
RUN gpasswd -a ubuntu sudo && \
    gpasswd -a ubuntu adm
RUN echo 'ubuntu ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/ubuntu

WORKDIR /tmp/work

# basic packages
RUN apt-get update -y
RUN apt-get install -y \
        git vim emacs \
        curl wget jq \
        tree tmux zsh \
        build-essential

# peco
RUN wget https://github.com/peco/peco/releases/download/v0.3.5/peco_linux_amd64.tar.gz &&\
    tar zxvf peco_linux_amd64.tar.gz &&\
    sudo mv peco_linux_amd64/peco /usr/local/bin


###########
# user
###########

USER ubuntu
WORKDIR /tmp/work_ubuntu
ENV HOME /home/ubuntu

# oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" ; exit 0

# python
ADD pyenv_rc pyenv_rc
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv && \
    git clone git://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
RUN cat pyenv_rc >> $HOME/.zshrc && echo $HOME/.zshrc
RUN sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
RUN ~/.pyenv/bin/pyenv install 2.7.9
RUN ~/.pyenv/bin/pyenv install 3.5.1

# ruby
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv && \
    git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build && \
    sudo ~/.rbenv/plugins/ruby-build/install.sh
ENV PATH /root/.rbenv/bin:$PATH
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.zshrc
RUN echo 'eval "$(rbenv init -)"' >> ~/.zshrc
RUN ~/.rbenv/bin/rbenv install 2.2.0 
RUN ~/.rbenv/bin/rbenv global 2.2.0
RUN ~/.rbenv/bin/rbenv exec gem install bundler

RUN ls
# peco.d
ADD .peco.d /home/ubuntu/.peco.d
RUN sudo chown -R ubuntu:ubuntu ~/.peco.d
RUN echo '. ~/.peco.d/*' >> ~/.zshrc

# emacs
ADD emacs-init.el /home/ubuntu/.emacs.d/init.el
RUN sudo chown -R ubuntu:ubuntu ~/.emacs.d
RUN zsh -c "~/.pyenv/bin/pyenv global 2.7.9 && curl -fsSkL https://raw.github.com/cask/cask/master/go | ~/.pyenv/shims/python"
RUN echo 'export PATH="/home/ubuntu/.cask/bin:$PATH"' >> ~/.zshrc
RUN /bin/zsh -c "source ~/.zshrc && cd ~/.emacs.d; ~/.cask/bin/cask init; ~/.cask/bin/cask install"

# RUN
WORKDIR /home/ubuntu
CMD /bin/zsh
