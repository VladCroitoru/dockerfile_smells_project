FROM nvidia/cuda:10.0-devel
LABEL maintainer="José Antonio Perdiguero López <perdy@perdy.io>"

ENV APP=barrenero-miner-ether
ENV LC_ALL='C.UTF-8' PYTHONIOENCODING='utf-8'

# Install system dependencies
ENV RUNTIME_PACKAGES libidn11 python3.6 python3-pip
ENV BUILD_PACKAGES build-essential git curl libidn11-dev cmake
RUN apt-get update -m && \
    apt-get install -y --no-install-recommends software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y --no-install-recommends $RUNTIME_PACKAGES && \
    apt-get remove --purge -y software-properties-common && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* \
        /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin

# Create project dirs
RUN mkdir -p /srv/apps/$APP/logs
WORKDIR /srv/apps/$APP

# Install ethminer and python requirements
COPY Pipfile Pipfile.lock /srv/apps/$APP/
RUN apt-get update && \
    apt-get install -y --no-install-recommends $BUILD_PACKAGES && \
    git clone https://github.com/ethereum-mining/ethminer /tmp/ethminer && \
    cd /tmp/ethminer && \
    git submodule update --init --recursive && \
    mkdir build; cd build && \
    cmake .. -DETHASHCUDA=ON -DETHASHCL=OFF && \
    cmake --build . && \
    make install && \
    cd /srv/apps/$APP/ && \
    python3.6 -m pip install --no-cache-dir --upgrade pip pipenv && \
    pipenv install --system --deploy --ignore-pipfile && \
    apt-get remove --purge -y $BUILD_PACKAGES && \
    apt-get clean && \
    rm -rf /tmp/* \
        /var/tmp/* \
        /var/lib/apt/lists/* \
        /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin \
        $HOME/.cache/pip/* \
        /root/.hunter/

# Copy application
COPY . /srv/apps/$APP/

ENTRYPOINT ["./run"]
