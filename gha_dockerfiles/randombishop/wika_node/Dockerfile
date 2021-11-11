FROM debian:10-slim

# Install dependencies
RUN apt update
RUN apt install -y git clang curl libssl-dev llvm libudev-dev
RUN apt-get -y install procps
RUN apt-get -y install vim

# Install rust
RUN mkdir install
WORKDIR install
RUN curl https://sh.rustup.rs -sSf > sh.rustup.rs
RUN sh sh.rustup.rs -y
RUN /root/.cargo/bin/rustup default stable
RUN /root/.cargo/bin/rustup update
RUN /root/.cargo/bin/rustup update nightly
RUN /root/.cargo/bin/rustup target add wasm32-unknown-unknown --toolchain nightly

# Checkout substrate
RUN git clone -b v3.0.0 https://github.com/paritytech/substrate.git

# Copy and compile wika project
RUN mkdir /install/wika_node
WORKDIR /install/wika_node
COPY ./libs ./libs
COPY ./node ./node
COPY ./pallets ./pallets
COPY ./runtime ./runtime
COPY ./Cargo.toml .
RUN /root/.cargo/bin/cargo build --release

# Back to root directory
WORKDIR /
COPY ./start_chain .

# Start the blockchain
CMD python -m SimpleHTTPServer 8765



