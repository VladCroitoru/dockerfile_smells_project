FROM fedora:25

RUN dnf -y update && \
    dnf -y install vim bzip2 \
                   flatpak flatpak-builder && \
    dnf -y group install "Development Tools" && \
    dnf -y group install "C Development Tools and Libraries" && \
    dnf -y clean all

ARG user=flatpak
RUN useradd --create-home --shell '/bin/bash' $user && \
    usermod $user -a -G wheel
USER $user
WORKDIR /home/$user
VOLUME /home/$user

ENTRYPOINT ["/bin/bash"]
