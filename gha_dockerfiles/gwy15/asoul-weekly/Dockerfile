# bullseye 才有 opencv 4.5； 4.2及以前有一个bug（imdecode 不识别 flags）
# build
FROM rust:slim-bullseye as builder
WORKDIR /code
ENV SQLX_OFFLINE=1
RUN apt-get update \
    && apt-get install -y \
        libopencv-dev \
        clang libclang-dev

COPY . .
RUN cargo b --release --no-default-features --features rustls --bin asoul_weekly \
    && strip target/release/asoul_weekly \
    && echo "Required dynamic libraries: " \
    && ldd target/release/asoul_weekly

# 
FROM debian:bullseye-slim
WORKDIR /code
RUN apt update \
    && apt-get install -y libopencv-core4.5 libopencv-imgproc4.5 libopencv-imgcodecs4.5 libopencv-videoio4.5 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /code/target/release/asoul_weekly .
COPY --from=builder /code/log4rs.yml .

ENTRYPOINT [ "./asoul_weekly" ]
CMD []
