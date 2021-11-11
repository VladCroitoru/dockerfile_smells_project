##
# We start from the basic hhvm image.
##
FROM hhvm/hhvm:3.18-lts-latest

# setup the root home
ENV HOME /root

# Turn off apt-get being prompty
ENV DEBIAN_FRONTEND noninteractive

# Copy over the template files for the sql and the shell scripts to initialize the image
COPY mysql_create_test_database.sql /tmp
COPY mysql_create_test_database.sh /tmp
COPY postgres_create_test_database.sql /tmp
COPY postgres_create_test_database.sh /tmp
COPY setup-image.sh /tmp

# Make the scripts executable
RUN chmod +x /tmp/mysql_create_test_database.sh /tmp/postgres_create_test_database.sh /tmp/setup-image.sh && \
    /tmp/setup-image.sh
