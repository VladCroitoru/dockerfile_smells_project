FROM soloincc/alpine-python-wkhtmltopdf-data-analysis:latest

MAINTAINER Wangoru Kihara wangoru.kihara@badili.co.ke

RUN apk add tzdata

# configure timezone data
RUN cp /usr/share/zoneinfo/Africa/Nairobi /etc/localtime
RUN echo "Africa/Nairobi" >  /etc/timezone

## default variables
ARG APP_DIR=/opt/tafiti

# Create the temp folder
RUN mkdir -p /opt/tafiti/tmpfiles

# Copy the requirements file and install the requirements
ADD requirements.txt /opt/tafiti/
RUN pip install -r /opt/tafiti/requirements.txt

# Change to the static dir and install the npm packages
WORKDIR /opt/tafiti/analyser/static
COPY analyser/static/package.json .
RUN npm install

# Return to the base folder
WORKDIR /opt/tafiti

# add (the rest of) our code
ADD . /opt/tafiti/