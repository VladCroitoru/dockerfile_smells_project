# curate-bids

FROM flywheel/bids-client:0.9.1
MAINTAINER Flywheel <support@flywheel.io>

# Install JQ to parse config file
RUN apk add --no-cache jq

# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run.py ${FLYWHEEL}/run.py
COPY manifest.json ${FLYWHEEL}/manifest.json

# Set the command for local runs
CMD python3 /flywheel/v0/run.py

