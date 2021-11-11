FROM rust
ADD ./bootstrap /app
WORKDIR /app
RUN cargo build --release

FROM ubuntu:20.04

LABEL maintainer="William Dussault <dalloriam@gmail.com>"

# Setup prereqs
RUN apt update && apt install -y libssl-dev fish unzip git curl sudo
COPY --from=0 /app/target/release/bootstrap /usr/bin/bootstrap
RUN useradd -ms /usr/bin/fish dev && passwd -d dev && usermod -aG sudo dev

USER dev
WORKDIR /home/dev
RUN yes | bootstrap all

RUN truncate --size 0 /home/dev/.dotfiles/config/fish/functions/fish_prompt.fish && sudo rm /usr/local/bin/starship

ENTRYPOINT "/usr/bin/fish"
