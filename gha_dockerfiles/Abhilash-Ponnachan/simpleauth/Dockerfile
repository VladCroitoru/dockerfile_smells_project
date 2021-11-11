FROM golang:1.17-alpine AS build
WORKDIR /authsimple
COPY go.mod *go.sum *.go ./
RUN CGO_ENABLED=0 go build -o ./authsrv

FROM alpine
WORKDIR /authsimple
COPY assets/ ./assets/
COPY db/ ./db/
COPY *.json ./
COPY --from=build /authsimple/authsrv ./
ENV PORT 8585
EXPOSE ${PORT}
#CMD tail -f /dev/null
CMD [ "./authsrv" ]