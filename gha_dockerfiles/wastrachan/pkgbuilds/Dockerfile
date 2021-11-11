FROM archlinux:latest
ARG BUILDUSER=build

RUN \
    pacman -Syyu --noconfirm && \
    pacman -S --noconfirm base-devel

RUN \
    useradd -m ${BUILDUSER} && \
    echo "${BUILDUSER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/${BUILDUSER}

COPY scripts/docker/docker-entrypoint.sh docker-entrypoint.sh
USER ${BUILDUSER}
VOLUME /pkg

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["makepkg", "--noconfirm", "--syncdeps", "--rmdeps", "--install", "--cleanbuild", "--clean"]
