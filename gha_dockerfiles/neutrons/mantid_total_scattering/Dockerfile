# Install mantid image
FROM mantidproject/mantid:nightly_ubuntu16.04_python3

# Copy git content from current branch
COPY . /root/mantid_total_scattering

# Add Mantid to python path
ENV MANTIDPATH         /opt/mantidnightly/bin
ENV TSREPO             /root/mantid_total_scattering
ENV PYTHONPATH         ${MANTIDPATH}:${TSREPO}:${PYTHONPATH}

# Install python dependencies
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install python3-pip curl git -y && \
    pip3 install pytest codecov

# Move to work directory
WORKDIR $TSREPO
