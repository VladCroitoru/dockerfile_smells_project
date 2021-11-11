FROM valentinbercot/docker-swift

LABEL name="docker-perfect" \
    description="docker-perfect help you to build applications running with perfect on ubuntu systems." \
    version="0.1.0" \
    maintainer="Valentin Bercot <valent1.bercot@gmail.com>"

# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    git \
    libssl-dev \
    openssl \
    uuid-dev && \
    rm -rf /var/lib/apt/lists/*

# Set Workdir to root
WORKDIR /
