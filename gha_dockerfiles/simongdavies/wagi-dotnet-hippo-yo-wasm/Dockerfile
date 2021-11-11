FROM mcr.microsoft.com/dotnet/sdk:5.0-focal

ARG USER_NAME=""
ENV USER ${USER_NAME:-demouser}

RUN mkdir /etc/sudoers.d && groupadd --gid 1000 ${USER} &&  useradd -s /bin/bash --uid 1000 --gid 1000 -m ${USER}  &&  echo ${USER}  ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USER}  && chmod 0440 /etc/sudoers.d/${USER} 

# Install Node.js

ARG NODE_VERSION="lts/*"
RUN su ${USER} -c "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh |  bash && chmod +x /home/${USER}/.nvm/nvm.sh"

WORKDIR /tmp

# Install hippo
ARG HIPPO_VERSION="v0.9.0"
RUN curl -fsSLo hippocli.tar.gz https://github.com/deislabs/hippo-cli/releases/download/${HIPPO_VERSION}/hippo-${HIPPO_VERSION}-linux-amd64.tar.gz && tar -xvf hippocli.tar.gz && mv hippo /usr/local/bin/  

# Install yo-wasm
RUN su ${USER} -c ". /home/${USER}/.nvm/nvm.sh && npm install -g yo && npm install -g generator-wasm"

# Install Rust 
RUN su ${USER} -c "umask 0002 && cd /tmp && mkdir rust && cd rust && curl -fsSLo install_rust.sh https://sh.rustup.rs && chmod +x ./install_rust.sh  && ./install_rust.sh -y -t wasm32-wasi"
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && apt-get -y install --no-install-recommends gcc gcc-multilib

COPY --chown=1000:1000 ./Deislabs.WAGI.Templates.0.9.0-preview.nupkg .

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

USER 1000

WORKDIR /

ENTRYPOINT dotnet new --install /tmp/Deislabs.WAGI.Templates.0.9.0-preview.nupkg > /dev/null 2>&1 && /bin/bash