FROM babolivier/arch-pkg-env

# Git
RUN sudo pacman -Syu --noconfirm
RUN sudo pacman -S git --noconfirm

# Yaourt
RUN git clone https://aur.archlinux.org/package-query.git && cd package-query && makepkg -si --noconfirm
RUN git clone https://aur.archlinux.org/yaourt.git && cd yaourt && makepkg -si --noconfirm

# Custom dependencies
RUN yaourt -S nodejs-lts-bin cozy-management --noconfirm
