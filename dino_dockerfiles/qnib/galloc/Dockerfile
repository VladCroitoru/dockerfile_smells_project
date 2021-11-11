FROM qnib/alplain-golang AS build

WORKDIR /usr/local/src/github.com/qnib/galloc
COPY main.go ./
RUN go build

FROM qnib/alplain-init

ENV SKIP_ENTRYPOINTS=true
COPY --from=build /usr/local/src/github.com/qnib/galloc/galloc /usr/local/bin/
CMD ["/usr/local/bin/galloc"]
