FROM debian:8.0
MAINTAINER Emil Nilsson "eonilsson@gmail.com"
ENV REFRESHED_AT 2015-06-07

ENV DOCKER_USER docker
ENV ZSH_GIT  https://github.com/enil/enil-zsh-dotfiles.git
ENV VIM_GIT  https://github.com/enil/enil-vim-dotfiles.git
ENV TMUX_GIT https://github.com/enil/enil-tmux-dotfiles.git

RUN apt-get -qq update && apt-get install -y \
		zsh \
		vim \
		git \
		tmux \
		tree \
		sudo \
		man-db \
		manpages

RUN sed -E 's/%sudo(\s+ALL=\(ALL:ALL\)) ALL\s*/%sudo\1 NOPASSWD:ALL/' /etc/sudoers > /tmp/sudoers \
		&& visudo -c -f /tmp/sudoers \
		&& mv /tmp/sudoers /etc/sudoers

RUN useradd --create-home --user-group --shell /bin/zsh --groups sudo $DOCKER_USER
WORKDIR /home/$DOCKER_USER
USER $DOCKER_USER

RUN mkdir .dotfiles \
		&& cd .dotfiles \
		&& git clone $ZSH_GIT zsh && zsh/install.sh \
		&& git clone $VIM_GIT vim && vim/install.sh \
		&& git clone $TMUX_GIT tmux && tmux/install.sh

ENTRYPOINT [ "/usr/bin/zsh", "-i" ]

