FROM ubuntu:18.04
LABEL Maintainer="Daniel P. Clark <6ftdan@gmail.com>" \
      Version="1.1.5" \
      Description="Remote pair programming environment with Ruby, NodeJS, Yarn, Rust, VIM, RVM, neovim, tmux, SSH, and FishShell."

ENV USER root
ENV NODE_VERSION=10

# Start by changing the apt output, as stolen from Discourse's Dockerfiles.
RUN echo "debconf debconf/frontend select Teletype" | debconf-set-selections &&\
# Probably a good idea
    apt-get update &&\
# Basic dev tools (Custom VIM build needed for plugins)
    apt-get install -y sudo openssh-client git build-essential \
        gnupg2 man curl direnv software-properties-common libpq-dev\
        libncurses5-dev libgnome2-dev libgnomeui-dev wget pkg-config \
        libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libssl-dev \
        libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
        ruby-dev lua5.1 liblua5.1-0-dev libperl-dev nano tzdata \
        locales cmake exuberant-ctags &&\
 # Add repos for Node and Yarn
    curl -sL https://deb.nodesource.com/setup_$NODE_VERSION.x | bash - ;\
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - ;\
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list ;\
    apt-get update &&\
    apt-get install -y nodejs yarn &&\
# Clean up
    apt-get clean -y &&\
    apt-get autoremove -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV VIM_VERSION=v8.1.1700
ENV RUST_VERSION=1.36.0
ENV HOME=/home/dev

# Begin VIM build & install
RUN git clone https://github.com/vim/vim.git &&\
    cd vim &&\
    git checkout $VIM_VERSION &&\
    ./configure --with-features=huge \
                --enable-multibyte \
                --enable-rubyinterp=yes \
                --enable-pythoninterp=yes \
                --with-python-config-dir=/usr/lib/python3.7/config \
                --enable-perlinterp=yes \
                --enable-luainterp=yes \
                --enable-gui=gtk2 --enable-cscope --prefix=/usr &&\
    make VIMRUNTIMEDIR=/usr/share/vim/vim81 &&\
    make install &&\
    cd .. &&\
    rm -rf vim &&\
    update-alternatives --install /usr/bin/editor editor /usr/bin/vim 1 &&\
    update-alternatives --set editor /usr/bin/vim &&\
    update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1 &&\
    update-alternatives --set vi /usr/bin/vim &&\

# Install Rust
    mkdir /home/dev &&\
    curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain $RUST_VERSION &&\
    . /home/dev/.cargo/env

# More recent versions require Rust nightly
ENV RACER_VERSION=2.0.14

# Install Racer (Rust auto-completion for VIM)
RUN git clone https://github.com/phildawes/racer.git &&\
    cd racer &&\
    git checkout $RACER_VERSION &&\
    /home/dev/.cargo/bin/cargo build --release &&\
    mkdir /home/dev/bin &&\
    mv ./target/release/racer /home/dev/bin &&\
    cd .. &&\
    rm -rf racer

# All the VIM stuff
# Copy .vimrc
RUN curl -sL https://raw.githubusercontent.com/danielpclark/ruby-pair/master/.vimrc > /home/dev/.vimrc;\

# Install Vundle
    git clone https://github.com/VundleVim/Vundle.vim.git /home/dev/.vim/bundle/Vundle.vim;\

# Install VIM plugins
    vim +PluginInstall +qall &&\

# YouCompleteMe
    cd /home/dev/.vim/bundle/YouCompleteMe &&\
    ./install.py --clang-completer  \
                 --js-completer     \
                 --rust-completer &&\
    cd /home/dev &&\

# vimproc
    cd /home/dev/.vim/bundle/vimproc && make &&\
    cd /home/dev &&\

# # Haskell Stack
# RUN curl -SL -o /home/dev/stack-1.6.5-linux-x86_64.tar.gz \
#     https://github.com/commercialhaskell/stack/releases/download/v1.6.5/stack-1.6.5-linux-x86_64.tar.gz &&\
#     tar -xzf /home/dev/stack-1.6.5-linux-x86_64.tar.gz &&\
#     mv stack-1.6.5-linux-x86_64/stack /home/dev/bin/stack &&\
#     rm -rf stack-1.6.5-linux-x86_64*

# Manually update DB Ext plugin
    curl -L --create-dirs -o /home/dev/.vim/bundle/dbext.vim/dbext_2500.zip http://www.vim.org/scripts/download_script.php\?src_id=24935 &&\
    cd /home/dev/.vim/bundle/dbext.vim/ &&\
    unzip dbext_2500.zip &&\
    rm dbext_2500.zip &&\
    cd - &&\

# Set up for pairing with wemux and install neovim
    add-apt-repository ppa:neovim-ppa/unstable &&\
    apt-get update &&\
    apt-get install -y tmux neovim &&\
    git clone git://github.com/zolrath/wemux.git /usr/local/share/wemux &&\
    ln -s /usr/local/share/wemux/wemux /usr/local/bin/wemux &&\
    cp /usr/local/share/wemux/wemux.conf.example /usr/local/etc/wemux.conf &&\
    echo "host_list=(dev)" >> /usr/local/etc/wemux.conf &&\

# Install fish
    apt-get install -y fish &&\
    mkdir -p /home/dev/.config/fish &&\
    curl -L --create-dirs -o /home/dev/.config/fish/functions/fish_prompt.fish https://raw.githubusercontent.com/danielpclark/fish_prompt/master/fish_prompt.fish &&\
    echo "set PATH /home/dev/bin:$PATH" >> /home/dev/.config/fish/fish.config &&\

# Install a couple of helpful utilities
    apt-get install -y ack-grep &&\

# Set up SSH. We set up SSH forwarding so that transactions like git pushes
# from the container happen magically.
    apt-get install -y openssh-server &&\
    mkdir -p /var/run/sshd &&\
    echo "AllowAgentForwarding yes" >> /etc/ssh/sshd_config &&\

# Clean up
    apt-get clean -y &&\
    apt-get autoremove -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Fix for occasional errors in perl stuff (git, ack) saying that locale vars
# aren't set.
RUN locale-gen en_US en_US.UTF-8 && dpkg-reconfigure locales &&\

    useradd dev -d /home/dev -m -s /usr/bin/fish &&\
    adduser dev sudo &&\
    mkdir -p /etc/container_environment &&\
    echo /home/dev > /etc/container_environment/HOME &&\
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers &&\

# Ownership
    chown -R dev.dev /home/dev &&\
    chown -R dev.dev /var/lib/gems

USER dev

ENV RUBY_VERSION=2.6.3

RUN \
# Setup neovim
    ln -s /home/dev/.vim /home/dev/.config/nvim ;\
    ln -s /home/dev/.vimrc /home/dev/.config/nvim/init.vim ;\
 
# Install RVM
    sudo apt-get update &&\
    gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB &&\
    curl -SL https://get.rvm.io | bash -s stable --ruby=$RUBY_VERSION &&\
    curl -L --create-dirs -o /home/dev/.config/fish/functions/rvm.fish https://raw.github.com/lunks/fish-nuggets/master/functions/rvm.fish &&\
    echo "rvm default" >> /home/dev/.config/fish/config.fish &&\

# Clean up
    sudo apt-get clean -y &&\
    sudo apt-get autoremove -y &&\
    sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ngrok
RUN wget -O /home/dev/ngrok.zip https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip &&\
    unzip -d /home/dev/bin /home/dev/ngrok.zip &&\
    rm /home/dev/ngrok.zip &&\

# SSH script and startup script
    sudo curl -SL -o /etc/banner https://raw.githubusercontent.com/danielpclark/ruby-pair/master/banner &&\
    curl -SL -o /home/dev/bin/ssh_key_adder.rb https://raw.githubusercontent.com/danielpclark/ruby-pair/master/ssh_key_adder.rb &&\
    chmod +x /home/dev/bin/ssh_key_adder.rb &&\
    sudo rm -f /etc/service/sshd/down &&\
    echo '#!/bin/bash\n\
sudo /usr/sbin/sshd\n\
if [ -z "$1" ]; then\n\
  exec /usr/bin/fish -l\n\
else \n\
  /home/dev/bin/ngrok authtoken $1\n\
  exec /home/dev/bin/ngrok tcp 22\n\
fi' > /home/dev/bin/boot.sh &&\
    chmod +x /home/dev/bin/boot.sh &&\

# Locale
    sudo locale-gen "en_US.UTF-8"

# Install the Github Auth gem, which will be used to get SSH keys from GitHub
# to authorize users for SSH
RUN /bin/bash -c "source ~/.rvm/scripts/rvm;rvm use $RUBY_VERSION;gem install rake bundler github-auth git-duet seeing_is_believing --no-document"

# Expose SSH
EXPOSE 22

ENV USER dev

RUN echo "[[ -s \"\$HOME/.cargo/env\" ]] && source \"\$HOME/.cargo/env\" # Load Rust in to PATH" \
    >> $HOME/.bash_profile &&\
    echo "export PATH=\"\$HOME/bin:\$PATH\"" \
    >> $HOME/.bash_profile &&\
    echo "source $HOME/.bash_profile" >> $HOME/.bashrc &&\
    echo ". \"\$HOME/.cargo/env\" # Load Rust in to PATH" \
    >> $HOME/.config/fish/config.fish &&\
    echo "set -gx PATH \$HOME/bin \$PATH" \
    >> $HOME/.config/fish/config.fish

# Remove sudo privileges
RUN sudo gpasswd -d dev sudo

# Install the SSH keys of ENV-configured GitHub users before running the SSH
# server process.
SHELL ["/usr/bin/fish", "-l", "-c"]
CMD /home/dev/bin/ssh_key_adder.rb $AUTHORIZED_GH_USERS;\
    exec /home/dev/bin/boot.sh $NGROK
