FROM base/archlinux

# Source perlbin to setup PATH in a non-interactive session
COPY bashrc /root/.bashrc

# Set the entrypoint to a interactive shell 
# This is needed as the /etc/provile file has to be executed since PATH has to
# be modified for perl.
ENTRYPOINT ["/usr/bin/bash", "-ic"]


RUN pacman --noconfirm -Syu archlinux-keyring reflector rsync pacman-contrib && \
    reflector --verbose -l 200 -f 50 --sort rate | tee /etc/pacman.d/mirrorlist && \
    pacman --noconfirm -S sed grep which diffutils gawk gettext gzip tar file git && \
    pacman --noconfirm -S texlive-most biber minted && \
    pacman --noconfirm -S texlive-bin && \
    paccache -rk0

