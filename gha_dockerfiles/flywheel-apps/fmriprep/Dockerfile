#flywheel/fmriprep

############################
# Get the fmriprep algorithm from DockerHub
ARG VER=1.5.5
FROM poldracklab/fmriprep:${VER}
MAINTAINER Flywheel <support@flywheel.io>
ENV FMRIPREP_VERSION 1.5.5

# Remove expired LetsEncrypt cert
RUN rm /usr/share/ca-certificates/mozilla/DST_Root_CA_X3.crt && \
    update-ca-certificates
ENV REQUESTS_CA_BUNDLE "/etc/ssl/certs/ca-certificates.crt"

############################
# Install basic dependencies
RUN apt-get update && \
    apt-get -y install \
    jq \
    tar \
    zip \
    build-essential


############################
# Make directory for flywheel spec (v0)
ENV FLYWHEEL /flywheel/v0
RUN mkdir -p ${FLYWHEEL}
COPY run.py ${FLYWHEEL}/run.py
COPY manifest.json ${FLYWHEEL}/manifest.json
COPY utils ${FLYWHEEL}/utils



# Add the fmriprep dockerfile to the container
ADD https://raw.githubusercontent.com/nipreps/fmriprep/${FMRIPREP_VERSION}/Dockerfile ${FLYWHEEL}/fmriprep_${FMRIPREP_VERSION}_Dockerfile


############################
# Copy over python scripts that generate the BIDS hierarchy
COPY create_archive.py /flywheel/v0/create_archive.py
COPY create_archive_funcs.py /flywheel/v0/create_archive_funcs.py
RUN chmod +x ${FLYWHEEL}/*


############################
# Install the Flywheel SDK and BIDS client
COPY requirements.txt ${FLYWHEEL}/requirements.txt
RUN pip install -r ${FLYWHEEL}/requirements.txt && rm -rf /root/.cache/pip


############################
# ENV preservation for Flywheel Engine
RUN python -c 'import os, json; f = open("/tmp/gear_environ.json", "w"); json.dump(dict(os.environ), f)'


WORKDIR /flywheel/v0

# Set the entrypoint
ENTRYPOINT ["/usr/local/miniconda/bin/python3.7 /flywheel/v0/run.py"]
