FROM kdelfour/cloud9-docker
MAINTAINER Dusty Chadwick <me@dchadwick.com>

# ------------------------------------------------------------------------------
# Install additional tools 
RUN apt-get update && apt-get install vim-nox wget unzip git python-setuptools -y
RUN mkdir ~/.vim && git clone https://github.com/flazz/vim-colorschemes.git ~/.vim
COPY vimrc /root/.vimrc
RUN git clone http://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
RUN echo | vim +PluginInstall +qall && \ || true
RUN easy_install pip

# ------------------------------------------------------------------------------
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ------------------------------------------------------------------------------
# Expose ports.
EXPOSE 80
EXPOSE 443
EXPOSE 3000
EXPOSE 5000
EXPOSE 8000
EXPOSE 8080



