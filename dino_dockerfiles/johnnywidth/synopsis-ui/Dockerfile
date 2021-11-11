FROM golang:1.7

# Copy the local package files to the container workspace.
ADD . /go/src/github.com/johnnywidth/synopsis-ui

# Change workdir in container
WORKDIR /go/src/github.com/johnnywidth/synopsis-ui

# Get app dependency
RUN go get

# Install App
RUN go install

# Export some needed env vars
ENV HOST ""
ENV PORT 8080

ENV FILE "/data/config.json"
ENV OUTPUT "/data/output"
ENV THREAD 50

# Create volume directory
RUN mkdir /data
RUN mkdir /root/.ssh

# Add volume directory
VOLUME ["/data", "/root/.ssh"]

# Set container entrypoint
ENTRYPOINT /go/bin/synopsis-ui

# Set port that the container will listen
EXPOSE 8080
