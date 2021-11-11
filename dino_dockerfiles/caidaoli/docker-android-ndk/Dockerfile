FROM bitriseio/android-ndk
run apt-get install -y zsh vim
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#run zsh
#run git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
#run setopt EXTENDED_GLOB
#run for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}" done
#run chsh -s /bin/zsh
#add https://github.com/clvv/fasd/tarball/1.0.1 /root/fasd
#workdir /root/fasd
#run make
add zshrc /root/.zshrc
