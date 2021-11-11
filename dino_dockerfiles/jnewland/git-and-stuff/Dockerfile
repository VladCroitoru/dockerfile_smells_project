FROM debian:stable-slim@sha256:108675f84412ca43096b5b879e01bed7a806911f3236e9fd818a737adf2bf083
COPY Aptfile* /
RUN apt-get clean && apt-get update -qq && \
    : install the packages in the lockfile && \
    apt-get -y install $(cat ./Aptfile.lock | sed 's/#.*//' | grep -v -s -e "^:repo:" | tr '\n' ' ') || true && \
    : install the packages in the request file, should be a noop && \
    apt-get -y install $(cat ./Aptfile | sed 's/#.*//' | grep -v -s -e "^:repo:" | tr '\n' ' ') && \
    : generate an updated lockfile && \
    dpkg -l | grep ii | awk '{print $2 "=" $3}' > /Aptfile.lock && \
    : cleanup && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home app && \
    adduser app sudo && \
    echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
WORKDIR /home/app
USER app
