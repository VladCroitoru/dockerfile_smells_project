FROM trzeci/emscripten-slim:sdk-incoming-64bit

# gcc is necessary to be able to compile crates that have build scripts
RUN apt-get update && apt-get install -y curl gcc

RUN curl https://sh.rustup.rs -sSf | sh -s -- -y --default-toolchain stable
ENV PATH /root/.cargo/bin:$PATH

RUN rustup target add asmjs-unknown-emscripten
RUN rustup target add wasm32-unknown-emscripten
RUN rustup target add wasm32-unknown-unknown

RUN rustup toolchain install nightly
RUN rustup target add --toolchain nightly asmjs-unknown-emscripten
RUN rustup target add --toolchain nightly wasm32-unknown-emscripten
RUN rustup target add --toolchain nightly wasm32-unknown-unknown

COPY config /root/.cargo
COPY asmjs-emscripten-toolchain.cmake /root
