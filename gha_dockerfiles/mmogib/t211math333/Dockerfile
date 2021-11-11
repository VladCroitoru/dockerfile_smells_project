ARG JULIA_VERSION=1
FROM julia:${JULIA_VERSION}

########################################################
# Essential packages for remote debugging and login in
########################################################

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    apt-utils gcc g++ openssh-server cmake build-essential gdb \
    gdbserver rsync vim locales
RUN apt-get install -y bzip2 wget gnupg dirmngr apt-transport-https \
    ca-certificates openssh-server tmux && \
    apt-get clean

#setup ssh
RUN mkdir /var/run/sshd && \
    echo 'root:root_pwd' |chpasswd && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' \
    /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    mkdir /root/.ssh

#remove leftovers
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose 22 for ssh server. 7777 for gdb server.
EXPOSE 22 7777

# add user for debugging
RUN useradd -ms /bin/bash debugger
RUN echo 'debugger:debugger_pwd' | chpasswd

########################################################
# Add custom packages and development environment here
########################################################

# Options for common setup script
# Install zsh & Oh-My-Zsh
ARG INSTALL_ZSH="true"
# Upgrade OS packages to their latest versions
ARG UPGRADE_PACKAGES="true"
ARG COMMON_SCRIPT_SOURCE="https://raw.githubusercontent.com/microsoft/vscode-dev-containers/master/script-library/common-debian.sh"
ARG COMMON_SCRIPT_SHA="dev-mode"

# This Dockerfile adds a non-root user with sudo access. Update the “remoteUser” property in
# devcontainer.json to use it. More info: https://aka.ms/vscode-remote/containers/non-root-user.
ARG USERNAME=mshahrani
ARG USER_UID=1001
ARG USER_GID=$USER_UID

# Install needed packages and setup non-root user.
RUN apt-get update \
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl ca-certificates 2>&1 \
    && curl -sSL  ${COMMON_SCRIPT_SOURCE} -o /tmp/common-setup.sh \
    && ([ "${COMMON_SCRIPT_SHA}" = "dev-mode" ] || (echo "${COMMON_SCRIPT_SHA} */tmp/common-setup.sh" | sha256sum -c -)) \
    && /bin/bash /tmp/common-setup.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    && rm /tmp/common-setup.sh \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /julia-devcontainer-scripts
COPY ./postcreate.jl /julia-devcontainer-scripts
COPY .zshrc /root/.zshrc
RUN chmod +x /julia-devcontainer-scripts/postcreate.jl
########################################################

CMD ["/usr/sbin/sshd", "-D"]

#add support for English and Italian
#COPY locale.gen /etc/locale.gen
#RUN locale-gen