FROM archlinux/base:latest
MAINTAINER colajam93 <https://github.com/colajam93>

RUN pacman --noconfirm --needed -Syu \
        asp \
        base-devel \
        gdb \
        git \
        man-pages \
        openssh \
        python \
        rsync \
        unzip \
        vim &> /dev/null && \
    git clone --depth 1 https://github.com/colajam93/dotfiles.git &> /dev/null && \
    bash /dotfiles/install.sh -f -q simple &> /dev/null && \
    useradd -m test && \
    echo "test:test" | chpasswd && \
    echo 'test ALL=(ALL) ALL' >> /etc/sudoers
USER test
WORKDIR /home/test
RUN bash /dotfiles/install.sh -f -q simple &> /dev/null && \
    bash /dotfiles/install.sh -f -q develop &> /dev/null
