FROM golang:alpine3.14 as builder
WORKDIR /app
COPY ./fullcycle.go ./
RUN go build ./fullcycle.go

FROM hello-world:linux as runner
WORKDIR /app
COPY --from=builder ./app/fullcycle ./ 

ENTRYPOINT [ "./fullcycle" ]