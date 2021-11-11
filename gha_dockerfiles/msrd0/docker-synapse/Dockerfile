FROM rust:slim-bullseye AS healthcheck

RUN mkdir /src
WORKDIR /src
COPY Cargo.toml .
COPY Cargo.lock .
COPY src ./src
RUN cargo build --release --locked \
 && strip target/release/healthcheck

################################################################################

FROM debian:bullseye-slim

COPY matrix-org-archive-keyring.gpg /etc/apt/trusted.gpg.d/
RUN apt-get -y update \
 && apt-get -y install --no-install-recommends ca-certificates \
 && echo "deb [arch=amd64] https://matrix.org/packages/debian bullseye main" >/etc/apt/sources.list.d/matrix-org.list \
 && apt-get -y update \
 && apt-get -y install --no-install-recommends libgcc1 matrix-synapse-py3 pwgen python3-psycopg2 \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* /etc/matrix-synapse/* \
 && mkdir -p /etc/matrix-synapse/conf.d \
 && chown -R matrix-synapse /etc/matrix-synapse/

COPY homeserver.yml log.yml /etc/matrix-synapse/
COPY start.sh /usr/local/bin/
COPY version.sh /usr/local/bin/

EXPOSE 8008
VOLUME /etc/matrix-synapse/conf.d/
VOLUME /var/lib/matrix-synapse/

COPY --from=healthcheck /src/target/release/healthcheck /usr/local/bin/ealthcheck
HEALTHCHECK CMD ["/usr/local/bin/healthcheck"]

USER matrix-synapse
WORKDIR /var/lib/matrix-synapse/
CMD ["/usr/local/bin/start.sh"]
