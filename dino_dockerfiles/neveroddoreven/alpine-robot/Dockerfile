# Inspired by https://github.com/danielwhatmuff/robot-docker.git

FROM alpine:latest
RUN apk add --no-cache curl git ca-certificates

LABEL name="Docker image for the Robot Framework http://robotframework.org/"

# Install Python Pip and the Robot framework
RUN apk add --no-cache py-pip xvfb dbus chromium-chromedriver
RUN pip install --upgrade pip

RUN python --version

RUN pip install robotframework robotframework-selenium2library selenium robotframework-xvfb robotframework-requests robotframework-httplibrary 
    
