FROM skysider/pwndocker
USER root
COPY entrypoint.sh /opt
WORKDIR /opt
    # IOT 
RUN  apt-get update && apt-get install -y qemu-user  \
    qemu-user-static\
    # for aarch64 with debug symbol
    binutils-common=2.34-6ubuntu1.1\
    binutils-aarch64-linux-gnu\
    binutils-aarch64-linux-gnu-dbg \
    # aarch64 
    gcc-aarch64-linux-gnu\
    g++-aarch64-linux-gnu\
    libc6-dbg-arm64-cross\
    # for arm
    binutils-arm-linux-gnueabi-dbg \
    binutils-arm-linux-gnueabi\
    gcc-arm-linux-gnueabi\
    # mips 32 little ending
    gcc-mipsel-linux-gnu \
    g++-mipsel-linux-gnu \
    # mips 32 bit ending 
    gcc-mips-linux-gnu \ 
    g++-mips-linux-gnu \
    # mips 64 bit little ending
    gcc-mips64el-linux-gnuabi64\
    g++-mips64el-linux-gnuabi64 \
    # # mips 64 bit big ending
    gcc-mips64-linux-gnuabi64\
    g++-mips64-linux-gnuabi64\ 
    # IOT tools
    squashfs-tools\
    zlib1g-dev liblzma-dev liblzo2-dev\
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN sed -i "s|#PermitRootLogin yes|PermitRootLogin yes|g"  /etc/ssh/sshd_config && \
    echo "root:root" | chpasswd && chmod +x /opt/entrypoint.sh &&\
    ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    # config pwndbg 
    locale-gen en_US.UTF-8 && \
    printf "set context-code-lines 5\nset context-sections regs disasm code ghidra stack  expressions" >>/root/.gdbinit && \
    printf "\nexport LC_ALL=en_US.UTF-8\nexport PYTHONIOENCODING=UTF-8" >> /etc/profile &&\
    # coolpwn
    # git clone -b py3 https://github.com/ChristopherKai/coolpwn.git && cd coolpwn && python3 setup.py install && cd - &&\
    # mytool
    # git clone https://github.com/ChristopherKai/mytools.git && ln /opt/mytools/gentemplate/gentemplate.py /usr/local/bin/gentemplate &&\
    pip3 uninstall pwntools -y &&\
    git clone https://github.com/Gallopsled/pwntools.git  --depth=1 && cd pwntools && python3 setup.py install
    # formatStringExploiter

# web misc tools
RUN git clone https://github.com/Rup0rt/pcapfix.git --depth=1 && cd pcapfix && make && make install && cd -\
    && git clone https://github.com/brendan-rius/c-jwt-cracker.git  --depth=1 && cd c-jwt-cracker && make && cd - \
    # IOC
    && git clone https://github.com/ReFirmLabs/binwalk.git --depth=1 &&  cd binwalk &&  python3 setup.py install && cd -\
    && git clone https://github.com/devttys0/sasquatch && cd sasquatch && ./build.sh && cd - \
    # crypto
    && pip3 install pycryptodome 

EXPOSE 22
ENTRYPOINT [ "/opt/entrypoint.sh" ]