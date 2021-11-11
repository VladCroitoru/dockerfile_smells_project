FROM kalilinux/kali-linux-docker
MAINTAINER Yu-Cheng (Henry) Huang

SHELL ["/bin/bash", "-c"]

RUN dpkg --add-architecture i386 && \
    apt-get update && \
    echo "=== Installing essential packages ===" && \
    apt-get install -y man git git-core tmux bash-completion curl wget \
        p7zip-full python-pip python3-pip python-dev build-essential cmake \
        unzip xz-utils gcc g++ libc6-dev-i386 ruby-dev \
        lib32stdc++6 libxml2-dev libxslt1-dev libssl-dev \
        libpython2.7-dev libc6-dbg libc6-dbg:i386 sudo \
        gcc-multilib g++-multilib libcapstone3 libcapstone-dev \
        ncurses-dev e2tools qemu-system && \
    pip install --upgrade pip setuptools && \
    pip3 install --upgrade setuptools && \
    pip install --upgrade ipython pwntools ropgadget && \
    pip3 install --upgrade ipython pwntools ropgadget arm_now && \
    pushd ~ && \
    git clone https://github.com/Happyholic1203/dotfiles && \
    pushd ~/dotfiles && \
    chmod +x ./install.sh && \
    ./install.sh --with-ycm --with-ranger && \
    rm -rf ~/.vim/bundle/YouCompleteMe/third_party/ycmd/clang_archives/ && \
    echo "#!/bin/bash" > ~/init && \
    echo "TERM=xterm-256color tmux" >> ~/init && \
    echo "bash" >> ~/init && \
    chmod +x ~/init && \
    popd && \
    popd && \
    pushd ~ && \
    git clone https://github.com/scwuaptx/peda ~/peda && \
    git clone https://github.com/Happyholic1203/Pwngdb ~/Pwngdb && \
    git clone https://github.com/JonathanSalwan/ROPgadget ~/ROPgadget && \
    cp ~/Pwngdb/.gdbinit ~/ && \
    ipython profile create && \
    sed -i "s/.*\(c\.TerminalInteractiveShell\.editing_mode\).*/\1 = 'vi'/g" ~/.ipython/profile_default/ipython_config.py && \
    popd && \
    echo "=== Installing selected Kali packages ===" && \
    echo "[WEB]" && \
    apt-get install -yq sqlmap gobuster sublist3r dirb wfuzz xsser \
        exploitdb && \
    pushd ~ && \
    git clone https://github.com/Dionach/CMSmap && \
    pushd CMSmap && \
    pip3 install . && \
    popd && \
    python3 -c 'from cmsmap.lib.coreupdate import updater; updater.UpdateTmpCMS()' && \
    popd && \
    curl https://raw.githubusercontent.com/HA71/WhatCMS/master/whatcms.sh > /usr/local/bin/whatcms.sh && \
    chmod +x /usr/local/bin/whatcms.sh && \
    echo "[RECON]" && \
    apt-get install -yq whatweb nmap recon-ng wafw00f && \
    echo "[VA]" && \
    apt-get install -yq openvas wpscan sslscan nikto && \
    echo "[PASSWORD]" && \
    apt-get install -yq john hashcat hashcat-utils wordlists hydra seclists \
        medusa ncrack padbuster patator && \
    echo "[BINARY ANALYSIS]" && \
    apt-get install -yq gdb qemu ltrace strace gdbserver nasm binutils \
        radare2 afl && \
    gem install one_gadget && \
    echo "[SYMBOLIC EXECUTION]" && \
    apt-get install -yq python-z3 && \
    echo "[POST EXPLOITATION]" && \
    apt-get install -yq metasploit-framework webshells weevely && \
    echo "[MISC]" && \
    apt-get install -yq net-tools iputils-ping dnsutils netcat socat binwalk \
        mitmproxy nishang proxychains openvpn && \
    echo "Cleaning up" && \
    rm -f /var/cache/apt/archives/*.deb && \
    rm -rf /var/lib/apt/lists/*; rm -rf /tmp/*; rm -rf ~/.cache

RUN export tmp=$(mktemp -d) && \
    pushd $tmp && \
    wget https://github.com/vim/vim/archive/v8.1.0593.zip && \
    unzip *.zip && \
    pushd vim-* && \
    ./configure --with-features=huge \
                --enable-multibyte \
                --enable-pythoninterp=yes \
                --with-python-config-dir=$(echo /usr/lib/python2.7/config-*) \
                --enable-gui=gtk2 \
                --enable-cscope \
                --prefix=/usr/local && \
    make VIMRUNTIMEDIR=/usr/local/share/vim/vim81 && \
    make install && \
    rm -f /usr/bin/vi && \
    ln -sf `which vim` /usr/bin/vi && \
    popd && \
    popd && \
    rm -rf $tmp && \
    rm -f /var/lib/apt/lists/*; rm -rf /tmp/*; rm -rf ~/.cache

CMD ["/root/init"]
