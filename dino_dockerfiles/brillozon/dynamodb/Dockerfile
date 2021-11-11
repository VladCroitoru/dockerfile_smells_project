# Base image is JRE 8
FROM openjdk:8-jre

# Need curl for the local db software loading
RUN apt-get update &&  apt-get install curl

# Create the mount points for the code and data
RUN mkdir /dynamodb_code /dynamodb_data

# Install the code
RUN curl https://s3-us-west-2.amazonaws.com/dynamodb-local/dynamodb_local_latest.tar.gz | \
    tar zxf - -C /dynamodb_code

# Set the working directory to be the code directory
WORKDIR /dynamodb_code

# Execute the local version of dynamodb, putting data in the data volumne
CMD [ "/usr/bin/java", \
      "-Djava.library.path=/dynamodb_code", \
      "-jar", "DynamoDBLocal.jar", \
      "-dbPath", "/dynamodb_data" \
    ]

# Export the volumes
VOLUME [ "/dynamodb_code", \
         "/dynamodb_data"  \
       ]

