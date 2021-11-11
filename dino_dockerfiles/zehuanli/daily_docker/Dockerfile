FROM kalilinux/kali-rolling:latest
MAINTAINER Zehuan Li
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y net-tools wget curl socat iputils-ping traceroute lsof zip sudo ltrace strace procps
RUN apt-get install -y vim python3-dev python3-setuptools python3-pip python-dev python-setuptools python-pip
RUN apt-get install -y build-essential gcc-multilib gdb gdb-multiarch gdbserver
RUN apt-get install -y git-core
RUN apt-get install -y nmap ncat
RUN apt-get install -y tmux

RUN mkdir -p /root/tools
WORKDIR /root/tools
RUN git clone https://github.com/darkoperator/dnsrecon.git && \
    git clone https://github.com/ChrisTruncer/EyeWitness.git && \
    git clone https://github.com/SpiderLabs/Responder.git && \
    git clone --depth 1 https://github.com/drwetter/testssl.sh.git
RUN curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && \
    chmod 755 msfinstall && \
    ./msfinstall && \
    rm -rf msfinstall

RUN wget -O ~/.gdbinit-gef.py -q https://github.com/hugsy/gef/raw/master/gef.py && \
    echo source ~/.gdbinit-gef.py > ~/.gdbinit
RUN pip3 install pwntools ropper capstone unicorn ropgadget

RUN git clone https://github.com/lieanu/LibcSearcher.git && \
    cd LibcSearcher && \
    rm -rf libc-database && \
    git clone https://github.com/niklasb/libc-database.git && \
    cd libc-database && \
    ./get

RUN bash -c 'echo -e "color desert\nset cursorline\nhighlight cursorline cterm=none ctermbg=darkblue" > ~/.vimrc'
RUN bash -c 'echo -e "unbind C-b\nset-option -g prefix C-a\nbind-key a send-prefix\nbind-key C-a last-window" > ~/.tmux.conf'

ENV LC_CTYPE C.UTF-8
