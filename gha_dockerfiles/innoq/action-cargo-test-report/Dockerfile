# Copyright
FROM rust:buster as builder
RUN apt update
RUN apt install -y jq binutils busybox

WORKDIR /src
RUN git clone https://github.com/kingli-crypto/cargo2junit.git /src
RUN git checkout origin/feature/handle-ignore
RUN cargo install --target-dir /usr/local --path .
RUN cargo install --root /usr --path .

RUN ls -lah /usr/bin/cargo2junit
COPY create-rootfs.sh /usr/local/bin
RUN create-rootfs.sh /usr/bin/jq /bin/busybox /usr/bin/cargo2junit

# install busybox aliases so we have a usable system
RUN cd /tmp/rootfs/bin && ./busybox --install .

FROM scratch
COPY --from=builder /tmp/rootfs/ /
COPY markdown-summary.sh create-junit-report-and-summary.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/create-junit-report-and-summary.sh"]
