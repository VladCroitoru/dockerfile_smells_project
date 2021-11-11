FROM alpine:latest

RUN apk update --no-cache
RUN apk add \
      neovim \
      sudo bind-tools curl fd git jq \
      zsh bash go

# ENV
ENV ROOT /root
ENV GOPATH $ROOT/.go
ENV PATH $GOPATH/bin:$PATH

WORKDIR $ROOT

# shell
ADD shell .dotfiles/shell

RUN ln -s $ROOT/.dotfiles/shell/zshrc $ROOT/.zshrc
RUN $ROOT/.dotfiles/shell/get_antibody.sh -b /usr/local/bin

# nvim
RUN mkdir -p $ROOT/.config/nvim/colors
RUN mkdir -p $ROOT/.config/nvim/autoload

ADD vim/vimrcs/vimrc.triage $ROOT/.config/nvim/init.vim
ADD vim/plugin $ROOT/.config/nvim/plugin
ADD vim/colors/gruvbox.vim $ROOT/.config/nvim/colors

RUN curl -fLo ~/.config/nvim/autoload/plug.vim \
      https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

RUN nvim --headless +PlugInstall +qa

# Extra tools
RUN go get -u -ldflags "-w -s" github.com/taybart/fm
RUN go get -u -ldflags "-w -s" github.com/taybart/rest

