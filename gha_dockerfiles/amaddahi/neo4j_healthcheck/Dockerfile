# Inherit from the Python Docker image
FROM python:3.7

RUN pip3 install pandas
RUN pip3 install configobj
RUN pip3 install matplotlib

#RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc

# Install OpenJDK-8
RUN apt-get update && \
apt-get install -y openjdk-8-jdk && \
apt-get install -y ant && \
apt-get clean;

# Fix certificate issues
RUN apt-get update && \
apt-get install ca-certificates-java && \
apt-get clean && \
update-ca-certificates -f;
# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

#expose 7617

# Copy the source code to app folder
COPY ./neo4j_health /app/

# Change the working directory
WORKDIR /app/

# Set "python" as the entry point
ENTRYPOINT ["python3","./neo4j_health"]
#CMD echo "Hello world"
