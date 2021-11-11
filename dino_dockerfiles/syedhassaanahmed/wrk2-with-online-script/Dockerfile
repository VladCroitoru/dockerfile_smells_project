FROM alpine AS build
RUN apk add git build-base openssl-dev zlib-dev && \
    git clone https://github.com/giltene/wrk2.git && \
    cd wrk2 && make && mv wrk /bin/

FROM alpine AS final
LABEL maintainer="Syed Hassaan Ahmed"
COPY --from=build /bin/wrk /bin/wrk
RUN apk add --no-cache build-base && \
    apk add --update curl && \
    rm -rf /var/cache/apk/*

ENV SCRIPT_URL ""
ENV TARGET_URL ""
ENV WRK_OPTIONS ""
ENV WRK_HEADER "User-Agent: wrk"

CMD ["sh", "-c", "if [ \"$SCRIPT_URL\" != \"\" ]; then curl -sS ${SCRIPT_URL} > /tmp/script.lua; else echo \"\" > /tmp/script.lua; fi && wrk -s /tmp/script.lua ${WRK_OPTIONS} -H \"${WRK_HEADER}\" ${TARGET_URL}"]