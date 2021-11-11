FROM 169942020521.dkr.ecr.eu-west-1.amazonaws.com/base/golang:1.15-alpine-builder

FROM 169942020521.dkr.ecr.eu-west-1.amazonaws.com/base/golang:1.15-alpine-runtime

ADD assets ./assets

CMD ["-bind-addr=:4086"]

EXPOSE 4086
