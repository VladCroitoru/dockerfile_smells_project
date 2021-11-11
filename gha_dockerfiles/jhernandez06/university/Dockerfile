FROM golang:1.16 as builder

# Installing nodejs
RUN apk add --update nodejs-current curl bash build-base

# Installing Yarn
RUN curl -o- -L https://yarnpkg.com/install.sh | bash
ENV PATH="$PATH:/root/.yarn/bin:/root/.config/yarn/global/node_modules"

# Installing Ox
RUN go install github.com/wawandco/ox/cmd/ox@latest
WORKDIR /app
ADD . .

# Building the application binary in bin/app 
RUN ox build --static -o bin/app

FROM alpine
# Binaries
COPY --from=builder /app/bin/* /bin/

# For migrations use 
# CMD ox db migrate; app 
CMD app