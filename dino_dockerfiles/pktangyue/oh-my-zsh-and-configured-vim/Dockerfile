# Set the base image to CentOS 7
FROM centos:7

# Author
MAINTAINER pktangyue <tangyue1004@gmail.com>

# Change workdir to /root
ENV HOME /root

# Install needed package
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum update -y && yum install -y git zsh gcc make ruby ruby-devel lua lua-devel luajit luajit-devel ctags ncurses-devel perl perl-devel perl-ExtUtils-ParseXS perl-ExtUtils-XSpp perl-ExtUtils-CBuilder perl-ExtUtils-Embed the_silver_searcher

# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# Install vim74 with lua
RUN git clone https://github.com/vim/vim.git /root/vim
WORKDIR /root/vim
RUN ./configure --with-features=huge --enable-multibyte --enable-rubyinterp --enable-pythoninterp --enable-perlinterp --enable-luainterp --enable-gui=gtk2 --enable-cscope --with-tlib=ncurses --prefix=/usr
RUN make VIMRUNTIMEDIR=/usr/share/vim/vim74
RUN make install

# Install Vundle and launch my .vimrc
RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
COPY .vimrc /root/
RUN vim +PluginInstall +qall --not-a-term

# Goto /root
WORKDIR /root

# Clean
RUN rm -rf /root/vim \
    && yum clean all

# Add some config to .zshrc
RUN echo 'export EDITOR=vim' >> .zshrc \
    && echo 'export LESS=FRX' >> .zshrc \
    && echo 'alias vi=vim' >> .zshrc

# Use zsh
CMD ["zsh"]
