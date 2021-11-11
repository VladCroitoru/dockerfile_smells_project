# Base images
#FROM codercom/code-server:3.11.1 as code-server 
FROM codercom/code-server:3.8.1 as code-server
FROM prom/prometheus:v2.29.2 as prom
FROM prom/alertmanager:v0.23.0 as prom-am

####################################### ---

# Runtime
FROM nvcr.io/nvidia/cuda:11.4.1-runtime-ubuntu20.04

ENV \
    USER_NAME="Stefan Crain" \
    USER_EMAIL="stefan.crain@gmail.com" 

USER root
WORKDIR /tmp

# Update OS and install essential tools
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y \
        build-essential \
        ca-certificates \
        locales \
        sudo \
        tzdata \
    # os config
    && locale -a \
    && locale-gen en_US.UTF-8 \
    && dpkg-reconfigure locales \
    && locale -a \
    && update-ca-certificates \
    # create user
    && useradd \
        --create-home \
        --home /home/coder \
        coder \
    && groupadd docker \
    && groupmod -g 135 docker \
    && usermod -aG docker coder \
    && usermod -aG dialout coder \
    && echo 'coder ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers \
    # cleanup
    && apt-get remove -y \
        ca-certificates \
        locales \
        tzdata \
    && apt-get -qq clean autoclean \
    && apt-get -qq -y --purge autoremove \
    && chown -R coder:coder /home/coder \
    && rm -rf \
        /var/lib/apt/lists/* \
        /var/cache/apt/* 

ENV \
    LANG="en_US.utf8" \
    LANGUAGE="en_US.utf8"

# switch to user and install tools 
USER coder
WORKDIR /home/coder/

COPY --from=prom "/bin/promtool" "/bin/promtool"
COPY --from=prom-am "/bin/amtool" "/bin/amtool"
COPY --from=code-server "/usr/bin/code-server" "/usr/bin/code-server"
COPY --from=code-server "/usr/lib/code-server" "/usr/lib/code-server"

COPY --chown=coder "package.json" "package.json"
COPY --chown=coder "requirements.txt" "requirements.txt"

RUN export DEBIAN_FRONTEND=noninteractive \
    # using homebrew
    # which is stupid slow
    # so I can test the MAC experience
    && export HOMEBREW_MAKE_JOBS=16 \
    && export HOMEBREW_NO_INSTALL_CLEANUP=true \
    && export HOMEBREW_NO_AUTO_UPDATE=true \
    && export HOMEBREW_BUNDLE_BREW_SKIP="skopeo podman qemu bash bash-completion trash docker dockutil dark-mode act adwaita-icon-theme pyqt@5 uhd viennacl unrar terminal-notifier sshpass" \
    && export HOMEBREW_BUNDLE_CASK_SKIP="1password-cli alfred font-fira-code-nerd-font font-fira-code font-fira-mono-nerd-font iterm2  1password-cli alfred anaconda anybar appzapper balenaetcher blackhole brave-browser cinebench cubicsdr dash discord docker eul firefox font-fira-code font-fira-code-nerd-font font-fira-mono-nerd-font fritzing geekbench google-chrome imagealpha imageoptim iterm2 keka kicad kk7ds-python-runtime librepcb macs-fan-control micro-snitch obs rectangle serial slack spectacle spotify steam sublime-text synergy tor-browser visual-studio-code vlc xquartz" \
    && export HOMEBREW_BUNDLE_MAS_SKIP="" \
    && export HOMEBREW_BUNDLE_TAP_SKIP="homebrew/cask-fonts homebrew/cask homebrew/bundle homebrew/cask homebrew/cask-drivers homebrew/cask-fonts homebrew/cask-versions homebrew/core homebrew/services" \  
    # requirements for homebrew  
    && sudo apt-get update \
    && sudo apt-get install -y \
        curl \
        git \
    # homebrew
    && curl "https://raw.githubusercontent.com/stefancrain/dotfiles/main/Brewfile" -o "Brewfile" \
    && curl "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh" -o "Homebrew-install.sh" \
    && /bin/bash Homebrew-install.sh \
    && eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" \
    && brew bundle install --quiet || exit 0 \
    && brew link --overwrite inetutils \
    # node packages
    && npm install \
    # pip packages
    && pip3 install --no-cache-dir --upgrade --requirement requirements.txt \
    # cleanup
    && brew cleanup --prune=all -s \
    && apt-get remove -y \
        curl \
        git \
        sudo \
    && apt-get -qq clean autoclean \
    && apt-get -qq -y --purge autoremove \
    && rm -rf \
        /var/lib/apt/lists/* \
        /var/cache/apt/* \
        "$(brew --cache)" \
        Brewfile \
        Homebrew-install.sh \
        requirements.txt \
        package.json

COPY --chown=coder "code-server-settings.json" "/home/coder/.local/share/code-server/User/settings.json"

RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" \
    && code-server --install-extension "BriteSnow.vscode-toggle-quotes" \
    && code-server --install-extension "casualjim.gotemplate" \
    && code-server --install-extension "CoenraadS.bracket-pair-colorizer-2" \
    && code-server --install-extension "darkriszty.markdown-table-prettify" \
    && code-server --install-extension "DavidAnson.vscode-markdownlint" \
    && code-server --install-extension "dbaeumer.jshint" \
    && code-server --install-extension "dbaeumer.vscode-eslint" \
    && code-server --install-extension "eg2.vscode-npm-script" \
    && code-server --install-extension "Equinusocio.vsc-material-theme" \
    && code-server --install-extension "equinusocio.vsc-material-theme-icons" \
    && code-server --install-extension "erd0s.terraform-autocomplete" \
    && code-server --install-extension "esbenp.prettier-vscode" \
    && code-server --install-extension "exiasr.hadolint" \
    && code-server --install-extension "flesler.url-encode" \
    && code-server --install-extension "foxundermoon.shell-format" \
    && code-server --install-extension "GitLab.gitlab-workflow" \
    && code-server --install-extension "golang.go" \
    && code-server --install-extension "hashicorp.terraform" \
    && code-server --install-extension "HookyQR.beautify" \
    && code-server --install-extension "marcostazi.VS-code-vagrantfile" \
    && code-server --install-extension "mechatroner.rainbow-csv" \
    && code-server --install-extension "mikestead.dotenv" \
    && code-server --install-extension "ms-azuretools.vscode-docker" \
    && code-server --install-extension "ms-kubernetes-tools.vscode-kubernetes-tools" \
    && code-server --install-extension "ms-python.python" \
    && code-server --install-extension "ms-toolsai.jupyter" \
    && code-server --install-extension "njpwerner.autodocstring" \
    && code-server --install-extension "perragnaredin.light-plus-tweaked" \
    && code-server --install-extension "PKief.material-icon-theme" \
    && code-server --install-extension "redhat.vscode-yaml" \
    && code-server --install-extension "rubbersheep.gi" \
    && code-server --install-extension "ryu1kn.partial-diff" \
    && code-server --install-extension "samuelcolvin.jinjahtml" \
    && code-server --install-extension "Shan.code-settings-sync" \
    && code-server --install-extension "skyapps.fish-vscode" \
    && code-server --install-extension "sleistner.vscode-fileutils" \
    && code-server --install-extension "streetsidesoftware.code-spell-checker" \
    && code-server --install-extension "tushortz.python-extended-snippets" \
    && code-server --install-extension "wayou.vscode-todo-highlight" \
    && code-server --install-extension "wholroyd.HCL" \
    && code-server --install-extension "wholroyd.jinja" \
    && chezmoi init --one-shot --source ~/Code/.dotfiles stefancrain

# ENTRYPOINT [ "/home/linuxbrew/.linuxbrew/bin/fish" ]

EXPOSE 8080
WORKDIR /home/coder/project-data
ENTRYPOINT [ "code-server",  "--bind-addr", "0.0.0.0:8080" ]
