FROM alpine:3.2
ENTRYPOINT ["/bin/queryable"]

COPY . /src
RUN cd /src && ./build.sh "$(cat VERSION)" "$(cat VERSION_BUILD)"

ONBUILD RUN cd /src && ./build.sh "$(cat VERSION)-custom" "$(cat VERSION_BUILD)"
