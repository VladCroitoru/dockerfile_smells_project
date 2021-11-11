FROM ubuntu:groovy

LABEL maintainer="sneivandt"

ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y \
        ca-certificates \
        curl \
        exuberant-ctags \
        git \
        locales \
        openssh-client \
        shellcheck \
        tmux \
        vim \
        wget \
        zip \
        zsh \
    && rm -rf /var/lib/apt/lists/*

# Configure locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen

# Add user
RUN useradd -ms /bin/zsh sneivandt
WORKDIR /home/sneivandt
ENV SHELL /bin/zsh
ENTRYPOINT /usr/bin/zsh

# Install dotfiles
COPY --chown=sneivandt:sneivandt . /home/sneivandt/dotfiles
USER sneivandt
RUN /home/sneivandt/dotfiles/dotfiles.sh --install
