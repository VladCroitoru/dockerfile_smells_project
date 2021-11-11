ARG NODE_VERSION=16.8.0

FROM node:${NODE_VERSION} as rapidsnark-builder

WORKDIR /rapidsnark
RUN apt update && \
    apt install build-essential \
    libgmp-dev \
    libsodium-dev \
    nasm

COPY ./rapidsnark/*.json rapidsnark/tasksfile.js rapidsnark/tools ./
# COPY .rapidsnark/.git ./.git
COPY ./rapidsnark/depends ./depends
COPY ./rapidsnark/src ./src

# install the node deps
RUN npm install

# build the fields
RUN npx task createFieldSources

# build the provder
RUN npx task buildProver


# build container
FROM node:${NODE_VERSION} as zkcream-api

RUN apt update -y && \
    apt install -y build-essential \
    libgmp-dev \
    libsodium-dev \
    nasm

WORKDIR /api-server

ARG NODE_ENV
ENV NODE_ENV=$NODE_ENV

COPY package.json .
COPY tsconfig.json .
COPY yarn.lock .

RUN yarn install --quiet && \
    yarn cache clean --force

RUN mkdir zkcream \
    ts \
    abis && \
    mkdir -p zkcream/packages zkcream/scripts

COPY zkcream/packages /api-server/zkcream/packages/
COPY zkcream/scripts /api-server/zkcream/scripts/
COPY zkcream/*.json /api-server/zkcream/
COPY zkcream/*.lock /api-server/zkcream/
COPY ts ts/
COPY abis abis/

RUN yarn 

###
ENV NODE_ENV_BAK=$NODE_ENV

### TEMP build
ENV NODE_ENV=test

RUN cd zkcream && \
    yarn clean && \
    yarn && \
    yarn build

RUN cd zkcream/packages/contracts && \
    yarn migrate:docker

RUN cd zkcream/packages/circuits && \
    ./scripts/installZkutil.sh

COPY --from=rapidsnark-builder /rapidsnark/build/prover /api-server/rapidsnark/build/prover

RUN echo "Building api-server" && \
    yarn build