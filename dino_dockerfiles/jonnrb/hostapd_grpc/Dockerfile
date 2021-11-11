from quay.io/jonnrb/go as build
add . /src
run cd /src && go get ./cmd/hostapd_grpc

from gcr.io/distroless/static
copy --from=build /go/bin/hostapd_grpc /hostapd_grpc
copy --from=build /lib/libc* /lib/ld* /lib/
expose 8080 9090
entrypoint ["/hostapd_grpc"]
