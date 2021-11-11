FROM postgres:9.6

# Copy all of the SQL scripts into the container
COPY sql sql

# Copy the shell scripts into the container entry point.
# These will be run automatically.
COPY sh/init.sh /docker-entrypoint-initdb.d
