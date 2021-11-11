# Copy the local package files to the container's workspace.
FROM golang:alpine
# Create a container workspace.
RUN mkdir /go/src/potholes
# Copy the local package files to the container's workspace.
ADD potholes /go/src/potholes
# Set potholes as working directory
WORKDIR /go/src/potholes
# Build go binary
CMD ["go", "build"]