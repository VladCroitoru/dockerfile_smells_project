from mcluseau/golang-builder:1.16.2 as build
from alpine:3.13
entrypoint ["/bin/kingress"]
copy --from=build /go/bin/* /bin/
