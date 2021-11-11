FROM golang:alpine as build
# install additional tools
RUN apk add --no-cache musl-dev gcc
# copy files
COPY ./ /tmp/app
# save files
RUN mkdir /default \
&&  cp /tmp/app/config.yaml /default/config.yaml \
&& mv /tmp/app/entrypoint.sh /entrypoint.sh \
&& chmod +x /entrypoint.sh
# compilation
RUN mkdir -p /usr/local/go/src/github.com/khezen/ \
&&  mv /tmp/app /usr/local/go/src/github.com/khezen/bulklog \
&&  go build -o /bin/bulklog github.com/khezen/bulklog/cmd/srv

FROM alpine
COPY --from=build /default/config.yaml /default/config.yaml
COPY --from=build /entrypoint.sh /entrypoint.sh
COPY --from=build /bin/bulklog /bin/bulklog
RUN apk add --no-cache ca-certificates
ENV CONFIG_PATH /etc/bulklog
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bulklog"]
