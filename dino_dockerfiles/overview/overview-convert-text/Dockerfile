FROM alpine:3.7 AS os
RUN set -x \
  && apk add --update --no-cache \
    ca-certificates \
    python3 \
    py3-reportlab \
    py3-pygments \
    py3-chardet \
    poppler-utils


FROM overview/overview-convert-framework:0.0.15 AS framework
# multi-stage build


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/run
COPY --from=framework /app/convert-single-file /app/convert
COPY ./NotoSansMono-Regular.ttf /app/
COPY ./do-convert-single-file /app/
CMD [ "/app/run" ]


FROM base AS test
COPY --from=framework /app/test-convert-single-file /app/
COPY test/ /app/test/
RUN [ "/app/test-convert-single-file" ]
CMD [ "true" ]


FROM base AS production
