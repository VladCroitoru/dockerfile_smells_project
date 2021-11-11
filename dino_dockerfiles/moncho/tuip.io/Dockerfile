# build stage
FROM golang:alpine AS build-phase
ADD . /src
RUN cd /src && go build -o tuip

# final stage
FROM alpine
WORKDIR /app
COPY --from=build-phase /src/tuip /app/

EXPOSE 8000
ENTRYPOINT ./tuip
