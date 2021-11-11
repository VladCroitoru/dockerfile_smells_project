FROM alpine:latest as builder

RUN apk add gfortran make musl-dev --no-cache
COPY . /work

WORKDIR /work
RUN make
RUN chmod a+x /work/ewaldopt

# ------------------------------------------------------------------------------
FROM scratch

COPY --from=builder /work/ewaldopt /ewaldopt

ENTRYPOINT ["/ewaldopt"]
