##
##
## Arch Linux Baseimage + ArchAssault Repo
##
##

FROM base/archlinux:latest

RUN echo "[archassault]" >> /etc/pacman.conf && \
    echo "Server = http://repo.archassault.org/archassault/\$repo/os/\$arch" >> /etc/pacman.conf && \
    pacman-key -r CC1D2606 && \
    pacman-key --lsign CC1D2606 && \
    pacman -Sy --noconfirm archassault-keyring archassault-mirrorlist

##ENTRYPOINT ["/bin/bash"]
