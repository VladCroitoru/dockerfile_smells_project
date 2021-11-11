FROM archlinux:base-devel
COPY ./target/release/solana-logger .
COPY ./metaplex-studios-key.json .
ENTRYPOINT [ "/solana-logger" ]