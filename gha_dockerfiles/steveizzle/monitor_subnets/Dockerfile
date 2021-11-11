# build stage
FROM golang:alpine AS build-env
RUN apk --no-cache add build-base git mercurial gcc
ADD . /src
RUN cd /src && go build -o goapp

# final stage
FROM alpine
RUN addgroup -S mongroup && adduser -S monitoring -G mongroup
WORKDIR /app
COPY --from=build-env /src/goapp /app/
EXPOSE 2112
ENV AWS_MONITOR_SUBNETS $AWS_MONITOR_SUBNETS
ENTRYPOINT ./goapp
USER monitoring
