FROM python:3.8-slim-buster
LABEL maintainer="Keyko <root@keyko.io>"

ARG VERSION

RUN apt-get update \
    && apt-get install gcc gettext-base -y sudo cron curl git g++ nasm libgmp-dev libsodium-dev build-essential \
    && curl -sL https://deb.nodesource.com/setup_14.x | sudo bash - \
    && sudo apt-get -y install nodejs \
    && apt-get clean

RUN git clone https://github.com/nevermined-io/rapidsnark \
    && cd rapidsnark \
    && git submodule update --init --recursive \
    && sh ./scripts/install-linux.sh \
    && cd .. \
    && rm -rf rapidsnark

COPY . /nevermined-gateway
WORKDIR /nevermined-gateway

RUN pip install pip==20.2.4
RUN pip install .

# config.ini configuration file variables
ENV KEEPER_URL='http://127.0.0.1:8545'
ENV PARITY_URL='http://127.0.0.1:8545'
ENV SECRET_STORE_URL='http://127.0.0.1:12001'
ENV PROVIDER_ADDRESS=''
ENV PROVIDER_PASSWORD=''
ENV PROVIDER_KEYFILE=''
ENV RSA_PRIVKEY_FILE=''
ENV RSA_PUBKEY_FILE=''

ENV PROVIDER_BABYJUB_SECRET='abc'
ENV PROVIDER_BABYJUB_PUBLIC1='0x2e3133fbdaeb5486b665ba78c0e7e749700a5c32b1998ae14f7d1532972602bb'
ENV PROVIDER_BABYJUB_PUBLIC2='0x0b932f02e59f90cdd761d9d5e7c15c8e620efce4ce018bf54015d68d9cb35561'

ENV AZURE_ACCOUNT_NAME=''
ENV AZURE_ACCOUNT_KEY=''
ENV AZURE_RESOURCE_GROUP=''
ENV AZURE_LOCATION=''
ENV AZURE_CLIENT_ID=''
ENV AZURE_CLIENT_SECRET=''
ENV AZURE_TENANT_ID=''
ENV AZURE_SUBSCRIPTION_ID=''
# Note: AZURE_SHARE_INPUT and AZURE_SHARE_OUTPUT are only used
# for Azure Compute data assets (not for Azure Storage data assets).
# If you're not supporting Azure Compute, just leave their values
# as 'compute' and 'output', respectively.
ENV AZURE_SHARE_INPUT='compute'
ENV AZURE_SHARE_OUTPUT='output'

ENV GATEWAY_URL='http://0.0.0.0:8030'

# docker-entrypoint.sh configuration file variables
ENV GATEWAY_WORKERS='1'
ENV GATEWAY_TIMEOUT='9000'
ENV COMPUTE_API_URL='http://0.0.0.0:8050'

ENTRYPOINT ["/nevermined-gateway/docker-entrypoint.sh"]

EXPOSE 8030
