FROM golang:1.17

# Copy required app files
WORKDIR /app
COPY . .

# Build Server Binary and Clean up to slim image
RUN go mod tidy
RUN ./_scripts/build.sh && \
  rm -rf /go/pkg && \
  rm -rf ~/.cache/*

# Run Built Binary
ENTRYPOINT ["./build/server"]
