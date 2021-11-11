FROM quay.io/nyulibraries/primo-explore-devenv:2.0.0

ENV VIEW NYU
ENV DEVENV_PATH /app

WORKDIR /app/primo-explore/

# Installs Node modules, along with inner repository node_modules
COPY yarn.lock package.json ./
COPY custom/CENTRAL_PACKAGE/package.json ./custom/CENTRAL_PACKAGE/package.json
COPY custom/NYU/package.json ./custom/NYU/package.json
COPY custom/NYUAD/package.json ./custom/NYUAD/package.json
COPY custom/NYUSH/package.json ./custom/NYUSH/package.json
COPY custom/NYSID/package.json ./custom/NYSID/package.json
COPY custom/NYHS/package.json ./custom/NYHS/package.json
COPY custom/BHS/package.json ./custom/BHS/package.json
COPY custom/CU/package.json ./custom/CU/package.json

# Installs production version of dependencies from NPM
RUN yarn install --prod --frozen-lockfile --ignore-optional && yarn cache clean

# Copies remaining VIEW files
COPY ./custom/ ./custom/

# Sets up for running as a container
WORKDIR ${DEVENV_PATH}

EXPOSE 8004 3001