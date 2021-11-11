FROM debian:jessie
MAINTAINER Peter McConnell <me@petermcconnell.com>

RUN echo "deb http://ftp.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list && \
	apt-get update --fix-missing && \
	apt-get install -y \
	git \
	python \
	curl \
	vim-nox \
	cmake \
	sudo \
	bash-completion \
	docker.io \
	build-essential

# user dirs n stuff
RUN adduser --disabled-password --gecos '' dev && adduser dev sudo && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
	mkdir -p /home/dev /home/dev/Sites /home/dev/GoWorkspaces /home/dev/tmp /home/dev/bin && \
	touch /home/dev/.bash_history && \
	chown -R dev: /home/dev && \
	curl https://storage.googleapis.com/golang/go1.6.2.linux-amd64.tar.gz | tar -C /usr/local -zx

ENV PATH /home/dev/bin:$PATH
ENV GOROOT /usr/local/go
ENV GOPATH /home/dev/GoWorkspaces
ENV PATH /usr/local/go/bin:$PATH

USER dev
WORKDIR /home/dev

# vim config
RUN git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
	git clone https://github.com/pemcconnell/.dotfiles.git ~/.dotfiles && \
	cd ~/.dotfiles && \
	make install

# start 'er up with bash
CMD ["bash"]
