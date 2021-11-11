FROM gcr.io/distroless/base-debian11

ARG CMD_PATH

ENV ADDRESS "0.0.0.0:42700"

COPY ${CMD_PATH} /app

CMD ["/app"]