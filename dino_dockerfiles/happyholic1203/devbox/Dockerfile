FROM ubuntu:14.04
MAINTAINER Yu-Cheng (Henry) Huang

RUN apt-get update && \
    apt-get install -y man vim tmux git git-core bash-completion curl wget \
        python-pip python-dev build-essential ipython ctags ack-grep cmake \
        dh-make debhelper xz-utils python-sphinx && \
    pip install --upgrade pip pytest && \
	git clone --single-branch https://github.com/Happyholic1203/dotfiles && \
	cd dotfiles && \
	chmod +x ./install.sh && \
	./install.sh --with-ycm --with-ranger && \
	echo "#!/bin/bash" >> ~/init && \
	echo "TERM=xterm-256color tmux" >> ~/init && \
	echo "bash" >> ~/init && \
	chmod +x ~/init

CMD ["/root/init"]
