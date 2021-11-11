FROM golang:1.16.2-alpine3.12 AS builder

ARG CI_PROJECT_NAME
ARG GROUP
ARG CI_PIPELINE_ID

WORKDIR /go/src/$CI_PROJECT_NAME
COPY $GROUP/$CI_PROJECT_NAME/$CI_PROJECT_NAME .

RUN go version
RUN go build -tags=jsoniter -ldflags="-X 'main.Build=${CI_PIPELINE_ID}'"

FROM alpine:latest
RUN apk --no-cache add ca-certificates
# set local date to Europe/Moscow
RUN apk add --no-cache tzdata
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

ARG CI_PROJECT_NAME
ARG NODE_ENV
ARG PRJ

WORKDIR /
COPY --from=builder /go/src/${CI_PROJECT_NAME}/${CI_PROJECT_NAME} .
COPY --from=builder /go/src/${CI_PROJECT_NAME}/configs/${PRJ}/* ./configs/
COPY --from=builder /go/src/${CI_PROJECT_NAME}/migrations/* ./migrations/
COPY --from=builder /go/src/${CI_PROJECT_NAME}/certificates/* ./certificates/
ADD db_conf/${CI_PROJECT_NAME}-${NODE_ENV}/configs/* ./configs/
# https://stackoverflow.com/questions/35560894/is-docker-arg-allowed-within-cmd-instruction
ENV CI_PROJECT_NAME ${CI_PROJECT_NAME}
CMD ./${CI_PROJECT_NAME} -env=${NODE_ENV} -port=${PORT}
