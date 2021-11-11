FROM haskell:8.6.5

# Copy source into Docker image
COPY ./ /home/app/
WORKDIR /home/app

RUN apt-get update
RUN apt-get install -y sqlite3 libsqlite3-dev

# Install all dependencies and build project
RUN stack build

EXPOSE 8080

# Start server
CMD ["/usr/local/bin/stack", "exec", "silver-magpie-backend"]
