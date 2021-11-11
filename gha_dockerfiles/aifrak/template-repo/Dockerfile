FROM node:16.13.0-buster as node
RUN npm install -g npm@8.1.2 --quiet

FROM koalaman/shellcheck:v0.8.0 as shellcheck
FROM mvdan/shfmt:v3.4.0 as shfmt
FROM hadolint/hadolint:v2.8.0 as hadolint

FROM ubuntu:focal-20211006 as base

USER root

ENV INSIDE_DOCKER=1
ENV LANG=en_US.UTF-8

# 1. Install packages
# 2. Install setup locales
# 3. Clean
RUN set -e \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get update -qq \
  && apt-get install -y -qq --no-install-recommends \
    git=1:2.25.1-* \
    locales=2.31-* \
    parallel=20161222-* \
  && sed -i "/${LANG}/s/^# //g" /etc/locale.gen \
  && locale-gen ${LANG} \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/lib/apt/lists/*

# Added here instead before `locale-gen` to avoid warnings
ENV LC_ALL=${LANG}

ENV USERNAME=app-user
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

ENV HOME=/home/${USERNAME}
ENV APP_DIR=/app

# 1. Add username and groupname
# 2. Create project directory and add ownership
RUN set -e \
  && groupadd --gid ${USER_GID} ${GROUPNAME} \
  && useradd --uid ${USER_UID} --gid ${USER_GID} --shell /bin/bash \
    --create-home ${USERNAME} \
  && mkdir ${APP_DIR} \
  && chown ${USERNAME}: ${APP_DIR}

# Add shellcheck
COPY --from=shellcheck --chown=root /bin/shellcheck /usr/local/bin/

# Add shfmt
COPY --from=shfmt --chown=root /bin/shfmt /usr/local/bin/

# Add hadolint
COPY --from=hadolint --chown=root /bin/hadolint /usr/local/bin/

# Add NodeJS (without yarn)
COPY --from=node --chown=root /usr/local/bin /usr/local/bin/
COPY --from=node --chown=root /usr/local/include /usr/local/include/
COPY --from=node --chown=root /usr/local/lib /usr/local/lib/
COPY --from=node --chown=root /usr/local/share /usr/local/share/
# Remove dead symbolic links from yarn
RUN find /usr/local/bin/. -xtype l -exec rm {} \; 2>/dev/null

USER ${USERNAME}

WORKDIR ${APP_DIR}

ENV CI=true

CMD [ "bash" ]

FROM base as dev

USER root

RUN set -e \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get update -qq \
  && apt-get install -y -qq --no-install-recommends \
    ca-certificates=* \
    gnupg2=* \
    openssh-client=* \
    sudo=* \
  && echo "${USERNAME}" ALL=\(root\) NOPASSWD:ALL >/etc/sudoers.d/"${USERNAME}" \
  && chmod 0440 /etc/sudoers.d/"${USERNAME}" \
  && apt-get clean \
  && apt-get autoremove \
  && rm -rf /var/lib/apt/lists/*

ENV CI=false

USER ${USERNAME}

FROM dev as vscode

WORKDIR ${HOME}

RUN set -e \
  && mkdir -p .vscode-server/extensions \
    .vscode-server-insiders/extensions

WORKDIR ${APP_DIR}
