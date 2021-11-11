# Base image for subsequent instruction.
FROM java:8

# Install gzip
RUN apt-get update
RUN apt-get -y install unzip

# Download gradle
RUN wget https://services.gradle.org/distributions/gradle-2.7-all.zip
RUN unzip gradle-2.7-all.zip 

# Copy the files from . to /src
ADD . /src

# Set the working directory for any run, cmd, entrypoin, copy and add
# instruction that follow.
WORKDIR /src

# Build the app
RUN export PATH=$PATH:/gradle-2.7/bin && gradle build

# Port will be listen by container
EXPOSE 8080

# Default actions for an executing container 
CMD ["java", "-jar", "/src/build/libs/hello-1.0.jar"]
