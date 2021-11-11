ARG NODE_IMG=node
ARG NODE_VER=lts
ARG PY_IMG=python
ARG PY_VER=3.7.9-stretch

FROM ${NODE_IMG}:${NODE_VER} as client
WORKDIR /project
COPY package.json yarn.lock ./
RUN yarn install
COPY . ./
RUN yarn build --production

FROM ${PY_IMG}:${PY_VER}
ARG NODE_VER=lts
# Set shell to use for run commands
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN curl -sL https://deb.nodesource.com/setup_${NODE_VER}.x | bash -

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  gettext \
  curl \
  build-essential \
  nodejs \
  ruby-sass \
  ruby-compass \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install python dependencies
WORKDIR /setup

# BUG: this is not being carried over from the builder somehow
COPY package.json yarn.lock ./
RUN npm install -g \
yuglify

# Use pip to install poetry. We don't use virtualenvs in the build context.
# Therefore, the vendored install provides no additional isolation.
RUN pip install --upgrade pip && \
  pip install \
  poetry~=1.1

COPY poetry.lock pyproject.toml /setup/
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install --no-dev --no-root

RUN mkdir /var/log/django
VOLUME ["/media"]
VOLUME ["/static"]

COPY . /project
WORKDIR /project
# translation messages, if necessary
RUN python manage.py compilemessages
# copy compiled JS assets
COPY --from=client /project/static/vue /project/static/vue
COPY --from=client /project/webpack-stats.json /project/webpack-stats.json

EXPOSE 80 443
