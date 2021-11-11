FROM golang:latest

# Setup general environment
ENV SHELL bash
ENV WORKON_HOME /usr/local/app
ENV DOCKER_NAME DEFAULT_NAME

# Make project folder
RUN mkdir ${WORKON_HOME}

# Copy all files
ADD src ${WORKON_HOME}

# Change work directory
WORKDIR ${WORKON_HOME}

# Install dependencies
RUN go get "github.com/gorilla/pat"

# Write version file
RUN echo "0.0" > version.dat

# Compile and execute the script
RUN go build server.go
CMD ["./server"]

# Open port
EXPOSE 1080