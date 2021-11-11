FROM sharkvan/devtools

MAINTAINER Tim Schruben tim.schruben@gmail.com

ENV LANG C.UTF-8

USER root
RUN yum install -y haskell-platform

WORKDIR $HOME/.vim/bundle

RUN git clone https://github.com/lukerandall/haskellmode-vim.git
USER $USER
WORKDIR $HOME
