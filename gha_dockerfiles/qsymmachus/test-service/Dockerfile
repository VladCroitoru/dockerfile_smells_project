# 1. First step in multistage build, compile the source:
FROM golang:1.16 as build

# Copy app source code and build
WORKDIR /app
COPY server.go .
COPY go.mod .
COPY go.sum .
RUN go mod download

RUN go build -o server .

# 2. Second step, copy the compiled binary but leave the source behind:
FROM golang:1.16

WORKDIR /app
COPY --from=build /app/server .

# Create 'app' user so we're not running as root.
# Boilerplate below creates a group, and adds a user with no home
# directory, password, or shell. We then make the user the owner
# of the working directory.
RUN groupadd -r app \
  && useradd -r -s /bin/false -g app app \
  && chown -R app:app /app

# Run the app
USER app
EXPOSE 8080
CMD ["/app/server"]
