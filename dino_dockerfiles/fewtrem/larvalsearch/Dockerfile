# This requires the following git repo jar to be installed...:
# https://github.com/axtimwalde/mpicbg.git

# Use an official Python runtime as a base image
FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive
 
RUN apt-get -q -y update && \
  apt-get upgrade -q -y && \
  apt-get install -q -y openjdk-8-jdk \
    libev4 libev-dev libpq-dev libldap2-dev libsasl2-dev libssl-dev \
    python-dev python-pip curl maven wget unzip

ENV JYTHON_VERSION 2.7.0

RUN curl -L "http://search.maven.org/remotecontent?filepath=org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -o jython_installer-${JYTHON_VERSION}.jar && \
    java -jar jython_installer-${JYTHON_VERSION}.jar -s -d /jython-${JYTHON_VERSION} && \
    ln -s /jython-${JYTHON_VERSION}/bin/jython /usr/bin && \
    rm jython_installer-${JYTHON_VERSION}.jar

RUN mkdir /plugin

RUN wget "https://github.com/axtimwalde/mpicbg/archive/master.zip" -O /plugin/master.zip
RUN unzip /plugin/master.zip -d /plugin/
RUN mvn -f /plugin/mpicbg-master/pom.xml -Djar.finalName=mpicLatest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
