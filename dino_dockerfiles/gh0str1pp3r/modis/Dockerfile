FROM alpine:latest

# Install Dependencies
RUN apk update \
 && apk add coreutils python3-dev ca-certificates gcc make linux-headers musl-dev ffmpeg libffi-dev libxslt-dev

# Add project source
ADD . /usr/src/Modis
WORKDIR /usr/src/Modis

# Create volume for mapping the config
VOLUME /usr/src/Modis

# Install pip dependencies
RUN pip3.6 install --upgrade -r requirements.txt

CMD python3.6 launcher.py