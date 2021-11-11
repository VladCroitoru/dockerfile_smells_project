FROM nipreps/fmriprep:20.2.4

LABEL maintainer="support@flywheel.io"

ENV FLYWHEEL /flywheel/v0
WORKDIR ${FLYWHEEL}

# Remove expired LetsEncrypt cert
RUN rm /usr/share/ca-certificates/mozilla/DST_Root_CA_X3.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE "/etc/ssl/certs/ca-certificates.crt"

# Save docker environ here to keep it separate from the Flywheel gear environment
RUN python -c 'import os, json; f = open("/flywheel/v0/gear_environ.json", "w"); json.dump(dict(os.environ), f)'

RUN apt-get update && \
    curl -sL https://deb.nodesource.com/setup_12.x | bash - && \
    apt-get install -y \
    zip \
    nodejs \
    tree && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g bids-validator@1.8.4 \
    esbuild@0.13.4 \
    esbuild-runner@2.2.1

# Python 3.7.1 (default, Dec 14 2018, 19:28:38)
# [GCC 7.3.0] :: Anaconda, Inc. on linux
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/pip

ENV PYTHONUNBUFFERED 1

# Copy executable/manifest to Gear
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils
COPY run.py ${FLYWHEEL}/run.py

# Configure entrypoint
RUN chmod a+x ${FLYWHEEL}/run.py
ENTRYPOINT ["/flywheel/v0/run.py"]
