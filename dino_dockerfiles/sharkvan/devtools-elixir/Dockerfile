FROM sharkvan/devtools:latest

MAINTAINER Tim Schruben <tim.schruben@gmail.com>

ENV WORKDIR /project
RUN sudo chown -R $USER:$USER $HOME
RUN mkdir -p $HOME/.vim/bundle 
RUN cd ~/.vim/bundle/ && \
    sudo git clone --depth 1 https://github.com/elixir-lang/vim-elixir

#This volume setting is here so that another container can run the elixir server and mount the volume
VOLUME $WORKDIR

WORKDIR $WORKDIR
