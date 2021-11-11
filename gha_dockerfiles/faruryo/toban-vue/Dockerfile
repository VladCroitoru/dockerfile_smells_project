FROM node:15.14.0-buster AS base

# ---------------------------------------------------------
FROM base AS devcontainer

ARG USERNAME=node
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG INSTALL_ZSH="true"
ARG SOURCE_SOCKET=/var/run/docker-host.sock
ARG TARGET_SOCKET=/var/run/docker.sock
ARG ENABLE_NONROOT_DOCKER="true"

COPY .devcontainer/scripts/*.sh /tmp/scripts/

RUN apt-get update \
    && /bin/bash /tmp/scripts/common-debian.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}" \
    && /bin/bash /tmp/scripts/docker-debian.sh "${ENABLE_NONROOT_DOCKER}" "${SOURCE_SOCKET}" "${TARGET_SOCKET}" "${USERNAME}" \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN npm install -g @vue/cli@4.5.6

RUN mkdir /commandhistory \
    && touch /commandhistory/.zsh_history \
    && chown -R $USERNAME /commandhistory \
    && echo 'HISTFILE=~/.zsh_history/commandhistory/.zsh_history' >> /home/$USERNAME/.zshrc

USER $USERNAME

ENTRYPOINT [ "/bin/bash", "-v", "/usr/local/share/docker-init.sh" ]
CMD [ "sleep", "infinity" ]

# ---------------------------------------------------------
FROM base AS build

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---------------------------------------------------------
FROM nginx:1.21.3-alpine as production

WORKDIR /app
COPY --from=build /app/dist /etc/nginx/html

EXPOSE 80
ENTRYPOINT ["nginx", "-g", "daemon off;"]
