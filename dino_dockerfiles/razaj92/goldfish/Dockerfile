FROM alpine:3.6

# Version of goldfish to install
ENV GOLDFISH_VERSION=v0.9.0

# Directory to put Goldfish binary in
WORKDIR /app

# Install Goldfish binary and clean up
RUN   apk --no-cache add \
      curl \
      openssl \
      ca-certificates && \
      curl -L -o goldfish https://github.com/Caiyeon/goldfish/releases/download/$GOLDFISH_VERSION/goldfish-linux-amd64 && \
      chmod +x ./goldfish

COPY entrypoint.sh .

#Set entrypoint to executable
RUN chmod +x ./entrypoint.sh

#Default port to expose
EXPOSE 8000

#Default command to run
ENTRYPOINT ["./entrypoint.sh"]
