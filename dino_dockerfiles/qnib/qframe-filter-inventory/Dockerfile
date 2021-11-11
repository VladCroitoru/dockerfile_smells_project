FROM qnib/uplain-golang

WORKDIR /usr/local/src/github.com/qnib/qframe-filter-inventory/
COPY main.go ./main.go
COPY lib/ ./lib/
COPY vendor/vendor.json ./vendor/vendor.json
RUN govendor fetch +m \
 && govendor build

FROM qnib/uplain-init

COPY --from=0 /usr/local/src/github.com/qnib/qframe-filter-inventory/qframe-filter-inventory \
     /usr/local/bin/
ENV SKIP_ENTRYPOINTS=true
CMD ["qframe-filter-inventory"]
