FROM zeroc0d3lab/centos-base-consul:latest
MAINTAINER ZeroC0D3 Team <zeroc0d3.team@gmail.com>

#-----------------------------------------------------------------------------
# Set Environment
#-----------------------------------------------------------------------------
ENV PATH_HOME=/home/docker \
    PATH_WORKSPACE=/home/docker/workspace

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
# Clean Up All Cache
#-----------------------------------------------------------------------------
RUN yum clean all

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
    && sudo /usr/bin/fc-cache -vf $HOME/.fonts/ \
    && sudo /usr/bin/fc-cache -vf /usr/share/fonts

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
# Setup TrueColors (Terminal)
#-----------------------------------------------------------------------------
COPY ./rootfs/root/colors/24-bit-color.sh /opt/24-bit-color.sh
RUN chmod a+x /opt/24-bit-color.sh; sync \
    && sudo /bin/sh /opt/24-bit-color.sh

#-----------------------------------------------------------------------------
# Cleanup 'root', 'opt' & 'tmp' folder
#-----------------------------------------------------------------------------
RUN rm -f /root/*.tar.gz

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
# Set Volume Docker Workspace Lite
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