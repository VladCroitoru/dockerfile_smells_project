FROM golang:1.9

RUN apt-get update && apt-get install -y python-pip jq
RUN pip install awscli

# Final clean up, remove apt-get metadata, clear tmp dir. This should be done for all containers always.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*