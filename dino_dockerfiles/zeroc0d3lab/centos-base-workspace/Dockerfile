FROM zeroc0d3lab/centos-base-consul:latest
MAINTAINER ZeroC0D3 Team <zeroc0d3.team@gmail.com>

#-----------------------------------------------------------------------------
# Set Environment
#-----------------------------------------------------------------------------
ENV VIM_VERSION=8.0.1207 \
    LUA_VERSION=5.3.4 \
    LUAROCKS_VERSION=2.4.3 \
    RUBY_VERSION=2.4.2 \
    COMPOSER_VERSION=1.5.2 \
    PATH_HOME=/home/docker \
    PATH_WORKSPACE=/home/docker/workspace

ENV RUBY_PACKAGE="rbenv"
    # ("rbenv" = using rbenv package manager, "rvm" = using rvm package manager)

USER root
#-----------------------------------------------------------------------------
# Set Group & User for 'docker'
#-----------------------------------------------------------------------------
RUN mkdir -p ${PATH_HOME} \
    && groupadd docker \
    && useradd -r -g docker docker \
    && usermod -aG root docker \
    && chown -R docker:docker ${PATH_HOME} \
    && mkdir -p ${PATH_HOME}/git-shell-commands \
    && chmod 755 ${PATH_HOME}/git-shell-commands

#-----------------------------------------------------------------------------
# Find Fastest Repo & Update Repo
#-----------------------------------------------------------------------------
RUN curl -L https://copr.fedorainfracloud.org/coprs/mcepl/vim8/repo/epel-7/mcepl-vim8-epel-7.repo \
      -o /etc/yum.repos.d/mcepl-vim8-epel-7.repo

RUN yum makecache fast \
    && yum -y update

#-----------------------------------------------------------------------------
# Install Workspace Dependency (1)
#-----------------------------------------------------------------------------
RUN yum -y install \
           --setopt=tsflags=nodocs \
           --disableplugin=fastestmirror \
         git \
         git-core \
         zsh \
         gcc \
         gcc-c++ \
         autoconf \
         automake \
         make \
         libevent-devel \
         ncurses-devel \
         glibc-static \
         fontconfig \
         kernel-devel \
         readline-dev \
         lua-devel \ 
         lzo-devel \
         vim* \

#-----------------------------------------------------------------------------
# Install MySQL (MariaDB) Library
#-----------------------------------------------------------------------------
         mysql-devel \

#-----------------------------------------------------------------------------
# Install PostgreSQL Library
#-----------------------------------------------------------------------------
### PostgreSQL 9.2 (default)###
         postgresql-libs \
         postgresql-devel \

### PostgreSQL 9.6 ###
    && rpm -iUvh https://yum.postgresql.org/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm \
    && yum install -y postgresql96-libs postgresql96-server postgresql96-devel \

#-----------------------------------------------------------------------------
# Install Workspace Dependency (2)
#-----------------------------------------------------------------------------
RUN yum -y install \
           --setopt=tsflags=nodocs \
           --disableplugin=fastestmirror \
         zlib \
         zlib-devel \
         patch \
         readline \
         readline-devel \
         libyaml-devel \
         libffi-devel \
         openssl-devel \
         bzip2 \
         bison \
         libtool \
         sqlite-devel

#-----------------------------------------------------------------------------
# Install NodeJS
#-----------------------------------------------------------------------------
# RUN yum -y install nodejs npm --enablerepo=epel \
RUN yum -y install https://kojipkgs.fedoraproject.org//packages/http-parser/2.7.1/3.el7/x86_64/http-parser-2.7.1-3.el7.x86_64.rpm nodejs 

#-----------------------------------------------------------------------------
# Download & Install
# -) bash_it (bash + themes)
# -) oh-my-zsh (zsh + themes)
#-----------------------------------------------------------------------------
RUN rm -rf /root/.bash_it \
    && rm -rf /root/.oh-my-zsh \
    && touch /root/.bashrc \
    && touch /root/.zshrc \
    && cd /root \
    && git clone https://github.com/Bash-it/bash-it.git /opt/.bash_it \
    && git clone https://github.com/speedenator/agnoster-bash.git /opt/.bash_it/themes/agnoster-bash \
    && git clone https://github.com/robbyrussell/oh-my-zsh.git /opt/.oh-my-zsh \
    && git clone https://github.com/bhilburn/powerlevel9k.git /opt/.oh-my-zsh/custom/themes/powerlevel9k \
    && cd /opt  \
    && tar zcvf bash_it.tar.gz .bash_it \
    && tar zcvf oh-my-zsh.tar.gz .oh-my-zsh \
    && cp /opt/bash_it.tar.gz $HOME \
    && cp /opt/oh-my-zsh.tar.gz $HOME \
    && cd $HOME \
    && tar zxvf $HOME/bash_it.tar.gz \
    && tar zxvf oh-my-zsh.tar.gz

#-----------------------------------------------------------------------------
# Download & Install
# -) tmux + themes
#-----------------------------------------------------------------------------
RUN rm -rf /opt/tmux \
    && rm -rf $HOME/.tmux/plugins/tpm \
    && touch $HOME/.tmux.conf \
    && git clone https://github.com/tmux/tmux.git /opt/.tmux \
    && git clone https://github.com/tmux-plugins/tpm.git /opt/.tmux/plugins/tpm \
    && git clone https://github.com/seebi/tmux-colors-solarized.git /opt/.tmux-colors-solarized \
    && cd /opt  \
    && tar zcvf tmux.tar.gz .tmux \
    && cp /opt/tmux.tar.gz $HOME \
    && cd $HOME \
    && tar zxvf tmux.tar.gz

RUN cd $HOME/.tmux \
    && /bin/sh autogen.sh \
    && /bin/sh ./configure \
    && sudo make \
    && sudo make install

#-----------------------------------------------------------------------------
# Install Font Config
#-----------------------------------------------------------------------------
RUN mkdir -p $HOME/.fonts \
    && mkdir -p $HOME/.config/fontconfig/conf.d/ \
    && mkdir -p /usr/share/fonts/local \
    && wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf -O $HOME/.fonts/PowerlineSymbols.otf \
    && wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf -O $HOME/.config/fontconfig/conf.d/10-powerline-symbols.conf \
    && cp $HOME/.fonts/PowerlineSymbols.otf /usr/share/fonts/local/PowerlineSymbols.otf \
    && cp $HOME/.fonts/PowerlineSymbols.otf /usr/share/fonts/PowerlineSymbols.otf \
    && cp $HOME/.config/fontconfig/conf.d/10-powerline-symbols.conf /etc/fonts/conf.d/10-powerline-symbols.conf \
    && /usr/bin/fc-cache -vf $HOME/.fonts/ \
    && /usr/bin/fc-cache -vf /usr/share/fonts

#-----------------------------------------------------------------------------
# Download & Install
# -) dircolors (terminal colors)
#-----------------------------------------------------------------------------
RUN git clone https://github.com/Anthony25/gnome-terminal-colors-solarized.git /opt/.solarized \
    && cd /opt  \
    && tar zcvf solarized.tar.gz .solarized \
    && cp /opt/solarized.tar.gz $HOME \
    && cd $HOME \
    && tar zxvf solarized.tar.gz

#-----------------------------------------------------------------------------
# Prepare Install Ruby
# -) copy .zshrc to /root
# -) copy .bashrc to /root
#-----------------------------------------------------------------------------
RUN git clone https://github.com/zeroc0d3/ruby-installation /opt/ruby_installer 

COPY ./rootfs/root/.zshrc /root/.zshrc
COPY ./rootfs/root/.bashrc /root/.bashrc
RUN sudo /bin/sh /opt/ruby_installer/install_ruby.sh

#-----------------------------------------------------------------------------
# Install Ruby Packages (rbenv/rvm)
#-----------------------------------------------------------------------------
RUN sudo /bin/sh /opt/ruby_installer/gems.sh

#-----------------------------------------------------------------------------
# Clean Up All Cache
#-----------------------------------------------------------------------------
RUN yum clean all

#-----------------------------------------------------------------------------
# Download & Install
# -) lua
# -) luarocks
# -) vim
# -) vundle + themes
#-----------------------------------------------------------------------------
COPY ./rootfs/opt/install_vim.sh /opt/install_vim.sh
# RUN sudo /bin/sh /opt/install_vim.sh

#-----------------------------------------------------------------------------
# Install Lua
#-----------------------------------------------------------------------------
RUN curl -L http://www.lua.org/ftp/lua-${LUA_VERSION}.tar.gz -o /opt/lua-${LUA_VERSION}.tar.gz \
    && curl -L http://luarocks.github.io/luarocks/releases/luarocks-${LUAROCKS_VERSION}.tar.gz \
         -o /opt/luarocks-${LUAROCKS_VERSION}.tar.gz

RUN cd /opt \
    && tar zxvf lua-${LUA_VERSION}.tar.gz \
    && tar zxvf luarocks-${LUAROCKS_VERSION}.tar.gz \
    && cd lua-${LUA_VERSION} \
    && make linux \
    && cd ../luarocks-${LUAROCKS_VERSION} \
    && ./configure \
    && make \
    && sudo make install
    
#-----------------------------------------------------------------------------
# Download & Install
# -) vim
# -) vundle + themes
#-----------------------------------------------------------------------------
RUN rm -rf /root/vim \
    && git clone https://github.com/vim/vim.git /root/vim \
    && cd /root/vim \
    && git checkout v${VIM_VERSION} \
    && cd src \
    && make autoconf \
    && ./configure \
    && make distclean \
    && make \
    && cp config.mk.dist auto/config.mk \
    && sudo make install \
    && sudo mkdir -p /usr/share/vim \
    && sudo mkdir -p /usr/share/vim/vim80/ \
    && sudo cp -fr /root/vim/runtime/** /usr/share/vim/vim80/

RUN curl -sSL https://raw.githubusercontent.com/zeroc0d3/vim-ide/master/step02.sh | sudo bash -s

RUN git clone https://github.com/dracula/vim.git /opt/vim-themes/dracula \
    && git clone https://github.com/blueshirts/darcula.git /opt/vim-themes/darcula \
    && mkdir -p /root/.vim/bundle/vim-colors/colors \
    && cp /opt/vim-themes/dracula/colors/dracula.vim /root/.vim/bundle/vim-colors/colors/dracula.vim \
    && cp /opt/vim-themes/darcula/colors/darcula.vim /root/.vim/bundle/vim-colors/colors/darcula.vim

RUN tar zcvf vim.tar.gz /root/vim /root/.vim \
    && mv vim.tar.gz /opt

#-----------------------------------------------------------------------------
# Install Javascipt Unit Test
#-----------------------------------------------------------------------------
RUN /usr/bin/npm install --global chai \
    && /usr/bin/npm install --global tv4 \
    && /usr/bin/npm install --global newman 

#-----------------------------------------------------------------------------
# Install Javascipt Packages Manager
#-----------------------------------------------------------------------------
RUN /usr/bin/npm install --global yarn \
    && /usr/bin/npm install --global bower \
    && /usr/bin/npm install --global grunt \
    && /usr/bin/npm install --global gulp \
    && /usr/bin/npm install --global yo

#-----------------------------------------------------------------------------
# Upgrade Javascipt Packages Manager
#-----------------------------------------------------------------------------
RUN /usr/bin/npm upgrade --global chai \
    && /usr/bin/npm upgrade --global tv4 \
    && /usr/bin/npm upgrade --global newman \
    && /usr/bin/npm upgrade --global yarn \
    && /usr/bin/npm upgrade --global bower \
    && /usr/bin/npm upgrade --global grunt \
    && /usr/bin/npm upgrade --global gulp \
    && /usr/bin/npm upgrade --global yo

#-----------------------------------------------------------------------------
# Install Composer PHP Packages Manager
#-----------------------------------------------------------------------------
RUN wget https://getcomposer.org/download/${COMPOSER_VERSION}/composer.phar -O /usr/local/bin/composer \
    && sudo chmod +x /usr/local/bin/composer

#-----------------------------------------------------------------------------
# Setup TrueColors (Terminal)
#-----------------------------------------------------------------------------
COPY ./rootfs/root/colors/24-bit-color.sh /opt/24-bit-color.sh
RUN chmod a+x /opt/24-bit-color.sh; sync \
    && sudo /bin/sh /opt/24-bit-color.sh

#-----------------------------------------------------------------------------
# Set Configuration
#-----------------------------------------------------------------------------
COPY rootfs/ /

#-----------------------------------------------------------------------------
# Cleanup 'root', 'opt' & 'tmp' folder
#-----------------------------------------------------------------------------
RUN rm -f /root/*.tar.gz \
    && rm -f /root/*.zip \
    && rm -f /opt/*.tar.gz \
    && rm -f /opt/*.zip \
    && rm -f /tmp/*.tar.gz \
    && rm -f /tmp/*.zip 

#-----------------------------------------------------------------------------
# Set PORT Docker Container
#-----------------------------------------------------------------------------
EXPOSE 22

#-----------------------------------------------------------------------------
# Set Volume Docker Workspace
#-----------------------------------------------------------------------------
VOLUME [${PATH_WORKSPACE}]

#-----------------------------------------------------------------------------
# Run Init Docker Container
#-----------------------------------------------------------------------------
ENTRYPOINT ["/init"]
CMD []

#-----------------------------------------------------------------------------
# Check Docker Container
#-----------------------------------------------------------------------------
# HEALTHCHECK CMD [ $(curl -sI -w '%{http_code}' --out /dev/null http://localhost:8500/v1/agent/self) == "200" ] || exit 1
HEALTHCHECK CMD --interval=5m --timeout=3s /etc/cont-consul/check || exit 1

## NOTE:
## *) Run vim then >> :PluginInstall
## *) Update plugin vim (vundle) >> :PluginUpdate
## *) Run in terminal >> vim +PluginInstall +q
##                       vim +PluginUpdate +q
