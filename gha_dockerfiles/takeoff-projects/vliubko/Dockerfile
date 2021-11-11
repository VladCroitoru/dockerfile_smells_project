# Please keep up to date with the new-version of Golang docker for builder
FROM golang:1.17.1-buster as base

#------------------------------
# stage for local development
#------------------------------
FROM base as dev

RUN apt update && apt upgrade -y && \
    apt install -y git \
    make openssh-client

WORKDIR /app 

RUN curl -fLo install.sh https://raw.githubusercontent.com/cosmtrek/air/master/install.sh \
    && chmod +x install.sh && sh install.sh && cp ./bin/air /bin/air

CMD air 

#------------------------------
# artifact builder stage
#------------------------------
FROM base AS builder
WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . .

RUN cd app && CGO_ENABLED=0 GOOS=linux go build -a -o oms-lite .

#------------------------------
# generate clean, final image for end users
#------------------------------
FROM gcr.io/distroless/base-debian10 as final
COPY --from=builder /app/app/oms-lite .

USER nonroot:nonroot

# executable
ENTRYPOINT [ "./oms-lite" ]
# arguments that can be overridden
# CMD [ "3", "300" ]
