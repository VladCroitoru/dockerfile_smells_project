FROM frolvlad/alpine-glibc

WORKDIR /game

COPY --from=remud-build /remud/target/release/remud /game/remud

# Persistent world/key storage
VOLUME [ "/game/world", "/game/keys" ]

# Used for Let's Encrypt HTTP auth, must be port 80 externally
EXPOSE 80/tcp
# Default Telnet port
EXPOSE 2004/tcp
# Default web port - optionally HTTPS w/the --tls option
EXPOSE 2080/tcp

ENV RUST_LOG="warn,remud_lib=info,remud=info"