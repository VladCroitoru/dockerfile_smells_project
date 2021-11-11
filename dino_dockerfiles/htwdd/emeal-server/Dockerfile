FROM swift:4 as builder

COPY . ./

RUN mkdir -p /build/lib && cp -R /usr/lib/swift/linux/*.so /build/lib
RUN swift build -c release && mv `swift build -c release --show-bin-path` /build/bin

FROM ubuntu:16.04

RUN apt-get -q update && \
    apt-get -q install -y \
    libatomic1 \
    libbsd0 \
    libcurl3 \
    libicu55 \
    libxml2 \
    && rm -r /var/lib/apt/lists/*

COPY --from=builder /build/bin .
COPY --from=builder /build/lib/* /usr/lib/
COPY --from=builder /Config ./Config

EXPOSE 8080

ENTRYPOINT [ "./Run" ]
CMD [ "serve", "--env=production" ]
