FROM ghcr.io/flatt-security/shisho-cli:v0.5.2 AS cli

# ----

FROM gcr.io/distroless/cc:debug

COPY --from=cli /shisho /shisho
COPY entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]