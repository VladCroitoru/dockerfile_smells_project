FROM debian:jessie
MAINTAINER Ryosuke Ito <rito.0305@gmail.com>

WORKDIR /root
RUN apt-get update && apt-get install -y git tmux tig vim wget ksh zsh gcc make editorconfig && apt-get autoremove -y
RUN wget 'https://thoughtbot.github.io/rcm/debs/rcm_1.3.0-1_all.deb' && dpkg -i 'rcm_1.3.0-1_all.deb' && rm -f 'rcm_1.3.0-1_all.deb'
ADD . dotfiles
RUN mkdir .dotfiles.original && mv .bashrc .profile .dotfiles.original
RUN env USER=root RCRC=dotfiles/rcrc rcup || true
RUN dotfiles/vim/bundle/neobundle.vim/bin/neoinstall
RUN /usr/bin/chsh -s /usr/bin/zsh
ENTRYPOINT ["/usr/bin/zsh"]
