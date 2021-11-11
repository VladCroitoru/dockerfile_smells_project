FROM ubuntu:14.04.4

# Install Prereq Packages
RUN apt-get update && apt-get install -y \
  wget \
  python-pip \
  git \
  fontconfig \
  vim \
  vim-gtk 

#Install Powerline
RUN pip install git+git://github.com/Lokaltog/powerline

#Install Powerline Font

RUN wget https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf

RUN mv PowerlineSymbols.otf /usr/share/fonts/
RUN fc-cache -vf
RUN mv 10-powerline-symbols.conf /etc/fonts/conf.d/

#Set Powerline in Bash Globally
RUN echo "if [ -f /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh ]; then\nsource /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh\nfi\n" >> /etc/bash.bashrc

#Set Powerline in Vim Globally
RUN echo "set rtp+=/usr/local/lib/python2.7/dist-packages/powerline/bindings/vim/ \nset laststatus=2 \nset t_Co=256" >> /etc/vim/vimrc

#Set the Vundle 
RUN mkdir /etc/vim/bundle
RUN git clone http://github.com/gmarik/vundle.git /etc/vim/bundle/vundle

#Install Plugins
RUN wget -P /etc/vim  https://raw.githubusercontent.com/afromavens/docker-vimide/master/vimrc/vimrc_vundle_plugins.local 
RUN echo "source /etc/vim/vimrc_vundle_plugins.local" >> /etc/vim/vimrc
RUN vim -c 'PluginInstall' -c 'qall' -c 'qa!'

#Configure the Plugins
RUN wget -P /etc/vim  https://raw.githubusercontent.com/afromavens/docker-vimide/master/vimrc/vimrc_vundle_configure_plugins.local 
RUN echo "source /etc/vim/vimrc_vundle_configure_plugins.local" >> /etc/vim/vimrc

ENTRYPOINT ["/usr/bin/vim"]