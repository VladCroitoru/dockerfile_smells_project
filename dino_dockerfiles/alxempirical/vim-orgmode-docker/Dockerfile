FROM ubuntu:14.04
RUN apt-get update && apt-get install -y vim wget git && apt-get clean
ENV HOME=/root
# Install pathogen
COPY vimrc $HOME/.vimrc
RUN for d in autoload bundle vimballs; do mkdir -p $HOME/.vim/$d ; done && \
    cd $HOME/.vim/autoload && \
    wget -q https://raw.githubusercontent.com/tpope/vim-pathogen/8c91196cfd9c8fe619f35fac6f2ac81be10677f8/autoload/pathogen.vim
# Install recommended scripts
WORKDIR $HOME/.vim/bundle
RUN git clone git://github.com/tpope/vim-speeddating && cd vim-speeddating && git checkout 426c792e479f6e1650a6996c683943a09344c21e && \
    cd .. && \
    git clone git://github.com/mattn/calendar-vim    && cd calendar-vim    && git checkout 32c474d402a64aab9734a645c48a60fd04c91192
# The vin script takes the name of a vim script and its id on vim.org/scripts,
# and downloads and installs it. It's ugly, but there doesn't seem to be an easy
# way to refer to these scripts by name
COPY ./vin $HOME/.vim/bundle/
RUN ./vin utl          9060 && ./vin tagbar  21362 && ./vin NrrwRgn 22795 && \
    ./vin SyntaxRange 23217 && ./vin orgmode 23662
# Example org-mode file, for testing
WORKDIR $HOME
RUN wget -q https://raw.githubusercontent.com/novoid/org-mode-workshop/master/featureshow/org-mode-teaser.org
