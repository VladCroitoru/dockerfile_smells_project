###########
# Builder #
###########
FROM rust:latest AS builder

WORKDIR /insomnia_bot
COPY src/ ./src
COPY Cargo.toml .
COPY Cargo.lock .
RUN cargo build --release


##########
# Runner #
##########
FROM almalinux:8

RUN dnf install -y 'dnf-command(config-manager)' epel-release \
    https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm \
    https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm
RUN dnf config-manager --set-enable powertools
RUN dnf install -y ffmpeg python3-pip
RUN pip3 install yt-dlp
RUN ln -s /usr/local/bin/yt-dlp /usr/local/bin/youtube-dl

WORKDIR /insomnia_bot
COPY --from=builder /insomnia_bot/target/release/insomnia-bot ./
ENTRYPOINT ["/insomnia_bot/insomnia-bot"]
