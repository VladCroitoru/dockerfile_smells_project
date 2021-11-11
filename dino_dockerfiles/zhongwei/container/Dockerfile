FROM ubuntu

LABEL maintainer="zhongwei99@163.com"

ENV DEBIAN_FRONTEND=noninteractive

#Update apt source and install basic tools
RUN sed -i s@/archive.ubuntu.com/@/mirrors.163.com/@g /etc/apt/sources.list \
      && apt clean \
      && apt update \
      && apt install -fy --no-install-recommends \
             ca-certificates \
             htop \
             wget \
             curl \
             git \
             zsh \
             emacs \
             vim \
             neovim \
             bat \
             sl \
             nnn \
             mc \
             nasm \
             fonts-powerline 

ENV LC_ALL C.UTF-8
ENV TERM xterm-256color

#Mofidy TimeZone
ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
      && dpkg-reconfigure --frontend noninteractive tzdata

#Install Oh My Zsh
ENV SHELL /bin/zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
      && git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k \
      && git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting \
      && git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions \
      && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
      && sed -i s@ZSH_THEME=\"robbyrussell\"@ZSH_THEME=\"powerlevel9k/powerlevel9k\"@ ~/.zshrc \
      && sed -i 's@plugins=(git)@plugins=(git zsh-syntax-highlighting zsh-autosuggestions)@' ~/.zshrc \
      && sed -i 's@# export PATH=@export PATH=/usr/games:@' ~/.zshrc \
      && chsh -s /usr/bin/zsh

#Install build-essential
RUN apt install -y build-essential 

#Install Go
RUN apt install -y golang-1.14-go \
    && ln -s /usr/lib/go-1.14/bin/go /usr/local/bin/go \
    && sed -i '$aexport GOPROXY="https://goproxy.cn/"' ~/.zshrc

#Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && sed -i '$aexport RUSTUP_DIST_SERVER=https://mirrors.ustc.edu.cn/rust-static' ~/.zshrc \
    && sed -i '$aexport RUSTUP_UPDATE_ROOT=https://mirrors.ustc.edu.cn/rust-static/rustup' ~/.zshrc \
    && sed -i '$aexport PATH="$PATH:$HOME/.cargo/bin"' ~/.zshrc \
    && sed -i 's@export PATH=@export PATH=$HOME/.cargo/bin:/usr/lib/cargo/bin:@' ~/.zshrc 

#Install Nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt install -y nodejs

#Install Spacevim
RUN curl -sLf https://spacevim.org/install.sh | bash \
#      && vim +'call dein#install()' +qall \
      && nvim --headless +'call dein#install()' +qall


#Install Spacemacs
RUN git clone https://github.com/syl20bnr/spacemacs /root/.emacs.d
COPY emacs-pkg-install.el /root/.emacs.d/emacs-pkg-install.el
COPY .spacemacs /root/.spacemacs
RUN emacs -nw -batch -u root -q -kill

##Clean
RUN rm -rf /var/lib/apt/lists/*
