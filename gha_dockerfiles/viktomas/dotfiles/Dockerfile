FROM ubuntu:16.04

RUN apt-get update 
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:neovim-ppa/stable
RUN apt-get update 
RUN apt-get install -y neovim
RUN apt-get install -y zsh
RUN apt-get install -y git
RUN add-apt-repository ppa:longsleep/golang-backports
RUN apt-get update
RUN apt-get install -y golang-go
RUN apt-get install -y build-essential cmake
RUN apt-get install -y python-dev python3-dev
RUN useradd -ms /bin/zsh tomas
USER tomas
WORKDIR home/tomas
ADD init_prezto.sh .
RUN ./init_prezto.sh
ADD .zshrc .profile /home/tomas/
ADD .vim/init.vim .config/nvim/init.vim
ADD .vim/autoload/plug.vim .config/nvim/autoload/plug.vim
RUN nvim +PlugInstall; echo ""
ENV GOPATH /home/tomas/go
CMD /bin/zsh
