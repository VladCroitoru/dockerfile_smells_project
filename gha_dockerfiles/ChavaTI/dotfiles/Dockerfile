FROM archlinux

# Install base
RUN echo -e '\n' | pacman -Syu base-devel python zsh cmake git unzip
# setup user build
RUN useradd -m build -s /bin/zsh
RUN echo "build ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN echo "root ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
USER build
WORKDIR /home/build
# Install neovim
RUN git clone https://github.com/neovim/neovim.git
RUN cd neovim && make CMAKE_BUILD_TYPE=RelWithDebInfo && sudo make install && cd
# Install plug
RUN sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
# Install zsh
RUN git clone https://aur.archlinux.org/oh-my-zsh-git.git
RUN cd oh-my-zsh-git && makepkg --noconfirm -rsi --install && cd
# run dotfile script
COPY . /home/build/dotfiles
RUN sudo chown build dotfiles/install.bash
RUN cd dotfiles && ./install.bash 1 && cd
# install nvim
RUN git clone https://aur.archlinux.org/nvm.git
RUN cd nvm && makepkg --noconfirm -rsi --install && cd
RUN source /usr/share/nvm/init-nvm.sh
CMD ["/bin/zsh"]
