# The archlinux/archlinux repo is updated daily:
FROM archlinux/archlinux:base-devel@sha256:f68b935ba9d21ecc47d668a5cc892e36a57545fe039d46640d72227bd84f8f86 AS base

COPY --chown=root:root /mirrorlist /etc/pacman.d/mirrorlist

RUN set -eux; \
  sed -i -e '\|NoExtract  = usr/share/man/\* usr/share/info/\*|d' /etc/pacman.conf; \
  grep -vq usr/share/man /etc/pacman.conf; \
  pacman -Suy --noconfirm; \
  echo Done

FROM base AS aur
RUN set -eux; \
  useradd -m -G wheel aur; \
  echo '%wheel ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/90-wheel-nopw; \
  echo 'PKGDEST=/home/aur/packages' >> /etc/makepkg.conf; \
  echo 'SRCDEST=/home/aur/src' >> /etc/makepkg.conf; \
  pacman -S --noconfirm git; \
  mkdir -p /home/aur/packages /home/aur/src /home/aur/work; \
  chown -R aur:aur /home/aur/*; \
  echo Done
USER aur
WORKDIR /home/aur/work

RUN set -eux; \
  gpg --keyserver hkps://keyserver.ubuntu.com --receive-keys \
    # Keys used to sign 1password-cli:
    # pub   rsa4096 2017-05-18 [SC] [expires: 2025-05-16]
    #       3FEF9748469ADBE15DA7CA80AC2D62742012EA22
    # uid           [ unknown] Code signing for 1Password <codesign@1password.com>
    3FEF9748469ADBE15DA7CA80AC2D62742012EA22 \
    # Key used to sign rdfind:
    # pub   rsa4096 2020-08-04 [SC] [expires: 2025-08-03]
    #       CC3C51BA88205B19728A6F07C9D9A0EA44EAE0EB
    # uid           [ unknown] Paul Dreik (private key) <paul@pauldreik.se>
    # uid           [ unknown] Rdfind <rdfind@pauldreik.se>
    # sub   rsa4096 2020-08-04 [E] [expires: 2025-08-03]
    CC3C51BA88205B19728A6F07C9D9A0EA44EAE0EB \
  ; \
  for PKG in \
    1password-cli \
    amazon-ecr-credential-helper \
    aws-cli-v2-bin \
    bazelisk \
    carvel-tools \
    circleci-cli-bin \
    conftest \
    dive \
    flux-bin \
    fswatch \
    go-yq \
    google-cloud-sdk \
    grpcui \
    istio-bin \
    kind-bin \
    mongodb-shell \
    nvm \
    opa \
    protoc-gen-go \
    rdfind \
    symlinks \
    terraform-docs-bin \
    tfenv \
  ; do ( \
    [ -e "$PKG" ] || git clone --depth=1 "https://aur.archlinux.org/$PKG.git" "$PKG"; \
    cd "$PKG"; \
    makepkg -cCs --noconfirm; \
  ); done; \
  echo Done

FROM base AS layer-img

ARG USER

RUN set -eux; \
  # This is needed to prevent the system from trying to configure on boot:
  ln -srf /usr/share/zoneinfo/America/Los_Angeles /etc/localtime; \
  useradd -m -G wheel $USER; \
  echo Done

COPY --chown=root:root --from=aur /home/aur/packages/* /tmp/aur/packages/
COPY --chown=root:root /extensions /tmp/extensions

RUN set -eux; \
  pacman -U --noconfirm /tmp/aur/packages/*; \
  # Install all the tools we need pre-configured:
  pacman -S --noconfirm \
    # To force manpages to be added:
    bash \
    bash-completion \
    bind \
    byobu \
    cmake \
    docker \
    docker-compose \
    ed \
    entr \
    flatbuffers \
    git \
    github-cli \
    gnu-netcat \
    go \
    graphviz \
    grpc-cli \
    jq \
    k9s \
    ko \
    kubectl \
    kubeseal \
    kustomize \
    lsof \
    man-db \
    man-pages \
    neovim \
    nodejs \
    npm \
    openssh \
    packer \
    pacman-contrib \
    pigz \
    postgresql-libs \
    protobuf \
    pyenv \
    python-pipenv \
    qrencode \
    rclone \
    restic \
    rsync \
    shellcheck \
    skopeo \
    socat \
    stow \
    # For xxd:
    vim \
    wget \
    whois \
    xorg-xauth \
    yapf \
  ; \
  tfenv install 0.13.5; \
  [ ! -e /tmp/extensions/post_install.sh ] || /tmp/extensions/post_install.sh; \
  echo Done

# Configure system:
COPY --chown=root:root /docker-host.socket /docker-host.service /usr/local/lib/systemd/system/
COPY --chown=root:docker /docker-daemon.json /etc/docker/daemon.json
COPY --chown=root:root /gpg-agent-dir.service /etc/systemd/user/gpg-agent-dir.service
RUN set -eux; \
  systemctl enable docker.socket; \
  systemctl enable docker-host.socket; \
  systemctl enable sshd.service; \
  # Make sure that the /var/run/user/$UID/gnupg dir exists unconditionally.
  systemctl enable --global gpg-agent-dir.service; \
  echo '%wheel ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/90-wheel-nopw; \
  # Allow the `user` user to be able to forward unix domain sockets on top of
  # existing sockets.
  echo 'Match User '$USER >> /etc/ssh/sshd_config; \
  echo '  StreamLocalBindUnlink yes' >> /etc/ssh/sshd_config; \
  # Enable X11 forwarding support as well:
  echo '  X11Forwarding yes' >> /etc/ssh/sshd_config; \
  # Also needed for X11 forwarding, but can't be in a match statement:
  sed -i -e 's|#AddressFamily any|AddressFamily inet|' /etc/ssh/sshd_config; \
  echo Done

# Configure user:
COPY --chown=$USER:$USER /generated/authorized_keys /home/$USER/.ssh/authorized_keys
COPY --chown=$USER:$USER /generated/gpg-public-keys.asc /home/$USER/gpg-public-keys.asc
RUN set -eux; \
  usermod -a -G docker $USER; \
  usermod -a -G tfenv $USER; \
  cat /etc/passwd; \
  find /home -type f; \
  chown -R $USER:$USER /home/$USER/.ssh; \
  chmod 700 /home/$USER/.ssh; \
  chmod 600 /home/$USER/.ssh/*; \
  sudo -u $USER gpg --import /home/$USER/gpg-public-keys.asc; \
  rm /home/$USER/gpg-public-keys.asc; \
  echo Done

# Prune a bunch of files:
RUN set -eux; \
  rm -rf /tmp/aur /tmp/extensions; \
  # Remove all cache files:
  paccache -rk0; \
  echo Done

FROM scratch AS img

# We make a single layer image with all the files:
COPY --from=layer-img / /
ENV container=docker
ENTRYPOINT ["/usr/lib/systemd/systemd"]
CMD ["--log-level=info", "--unit=multi-user.target"]
