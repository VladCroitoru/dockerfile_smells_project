ARG DEBIAN_DIST_NAME=debian
ARG DEBIAN_VERSION_NAME=buster
ARG SLIM_IMAGE_SUFFIX=-slim
ARG UBUNTU_VERSION_NAME=bionic

ARG NODE_VERSION=14
ARG LLVM_VERSION=13


FROM buildpack-deps:${DEBIAN_VERSION_NAME}-curl AS downloader

ARG NODE_VERSION
ARG LLVM_VERSION

WORKDIR /var/task/

ENV PATH ${PATH}:/root/.cargo/bin

RUN curl -fsSLo /tmp/setup "https://deb.nodesource.com/setup_${NODE_VERSION}.x" \
 && curl -sSLo /tmp/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
 && curl -ksSLo /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py


FROM ${DEBIAN_DIST_NAME}:${DEBIAN_VERSION_NAME}${SLIM_IMAGE_SUFFIX} AS release

ARG DEBIAN_FRONTEND=noninteractive

ARG DEPS="\
    autoconf \
    automake \
    g++ \
    gcc \
    libtool \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev \
    wget \
    binutils \
    software-properties-common \
    build-essential \
    libnss3-dev \
    zlib1g-dev \
    libgdbm-dev \
    libncurses5-dev \
    libssl-dev \
    libffi-dev \
    libreadline-dev \
    libsqlite3-dev \
    libbz2-dev \
    apt-utils \
    apt-transport-https \
    lsb-release \
    curl \
    gnupg \
"
ARG UBUNTU_VERSION_NAME

ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime
ENV PATH=${LAMBDA_TASK_ROOT}:/var/lang/bin:/usr/local/bin:/usr/bin:/bin:/opt/bin:${PATH}

COPY --from=downloader /tmp/setup /tmp/setup
COPY --from=downloader /tmp/get-pip.py /tmp/get-pip.py
RUN apt-get update -qq  \
 && apt-get install -qqy --no-install-recommends ${DEPS} ca-certificates \
 && chmod +x /tmp/setup \
 && /tmp/setup \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys BA6932366A755776 \
 && add-apt-repository "deb http://ppa.launchpad.net/deadsnakes/ppa/ubuntu ${UBUNTU_VERSION_NAME} main" \
 && apt-get update -qq \
 && apt-get install -qqy --no-install-recommends nodejs python3.9-dev python3 \
 && npm install -g yarn \
 && rm -rf /tmp/setup\
    libnss3 \
    libncurses5 \
    python3.9 \
 && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 \
 && update-alternatives --install /usr/bin/python python /usr/bin/python3 1\
 && yarn global add aws-lambda-ric \
 && apt-get install --no-install-recommends -qqy python3.9 python3.9-distutils \
 && apt-get autoremove --purge -qqy ${DEPS} python3.9-dev \
 && python /tmp/get-pip.py \
 && rm -rf /var/lib/apt/lists/* /var/log/apt/* /var/log/alternatives.log /var/log/dpkg.log /var/log/faillog /var/log/lastlog /tmp/get-pip.py \
 && mkdir -p /opt/extensions

COPY assets/bootstrap ${LAMBDA_TASK_ROOT}/bootstrap

RUN chmod +x "${LAMBDA_TASK_ROOT}/bootstrap"


WORKDIR ${LAMBDA_TASK_ROOT}

ENTRYPOINT [ "bootstrap" ]

FROM release

COPY --from=downloader /tmp/aws-lambda-rie /usr/bin/aws-lambda-rie

RUN chmod +x /usr/bin/aws-lambda-rie
