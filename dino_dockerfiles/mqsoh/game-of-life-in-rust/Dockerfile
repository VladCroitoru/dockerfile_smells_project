FROM debian:stretch as big-image

RUN apt update && apt install --assume-yes locales && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN apt-get update && apt-get install --assume-yes \
    curl \
    file \
    build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y && \
    echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc

RUN apt update && \
    apt install --assume-yes libncurses5-dev libncursesw5-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /workdir
COPY ./game-of-life /workdir
RUN /root/.cargo/bin/cargo build --release



FROM debian:stretch
LABEL author="Mason Staugler"
LABEL repository="https://github.com/mqsoh/game-of-life-in-rust"
LABEL usage="Run \"docker run -it --rm mqsoh/game-of-life-in-rust\". You might have to \"reset\" your shell. Sorry!"

RUN apt update && apt install --assume-yes locales && \
    sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY --from=big-image /workdir/target/release/game_of_life /bin/game_of_life
COPY --from=big-image /workdir/boards /boards
ENTRYPOINT [ "game_of_life" ]
