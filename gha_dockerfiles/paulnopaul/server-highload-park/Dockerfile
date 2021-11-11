FROM rust:1.55.0
EXPOSE 7878
WORKDIR /usr/src/server-highload-park
COPY ./src ./src
COPY ./httptest ./httptest
COPY ./Cargo.toml ./
RUN ls
RUN cargo build --release
RUN ulimit -n 10000
CMD ["./target/release/server-highload-park"]
