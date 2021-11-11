FROM alpine:latest
MAINTAINER Burgy Benjamin <https://twitter.com/minidfx>

# install pre depends
RUN apk add --no-cache -U git python python-dev curl && \
curl -s https://bootstrap.pypa.io/get-pip.py | python -

# Create the Pebble user
RUN adduser -D -g "" -G users pebble && \
    mkdir -p /home/pebble/.pebble-sdk && \
    mkdir -p /home/pebble/sandbox

# Clone the tool
RUN git clone https://github.com/pebble-examples/cards-example.git /home/pebble/cards_example

# Install the tool dependencies
WORKDIR /home/pebble/cards_example
RUN pip install -r requirements.txt

# Clean up
RUN rm -r /root/.cache

USER pebble

WORKDIR /home/pebble/sandbox
VOLUME  /home/pebble/sandbox

ENTRYPOINT ["/usr/bin/python", "/home/pebble/cards_example/tools/svg2pdc.py"]

CMD ["--help"]
