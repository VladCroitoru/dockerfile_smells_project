FROM mesosphere/kafka-client

# Install pandas
RUN \
    apt-get update && \
    apt-get install -y python-dev python-pip python-avro python-pandas python-snappy && \
    rm -rf /var/lib/apt/lists/*

# Install Faker, Click, fastavro
# FIXME: Use of pip and requirements.txt was abandandoned due to a weird crypto error.
RUN easy_install Faker click fastavro

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Define environment variable
ENV KAFKA_BROKER_LIST 127.0.0.1:1025
ENV KAFKA_TOPIC_NAME topic1
ENV INCIDENT_COUNT 1

CMD ["watch", "-n30", "./loadit.sh"]

