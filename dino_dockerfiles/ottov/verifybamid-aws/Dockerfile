FROM jfloff/alpine-python:2.7-slim

# Metadata
LABEL container.base.image="jfloff/alpine-python:2.7-slim"
LABEL software.name="verifybamid"
LABEL software.version=1.1.3
LABEL software.website="https://genome.sph.umich.edu/wiki/VerifyBamID"
LABEL tags="Genomics"

# Other software dependencies
RUN pip install boto3 awscli

# verifybamid binary dependency
RUN apk add --no-cache libstdc++

# Add pre-built (alpine) binary
COPY verifyBamID_1.1.3/verifyBamID/bin/verifyBamID /usr/local/bin/

# Application entry point
COPY run_verify.py /run_verify.py
COPY common_utils /common_utils

ENTRYPOINT ["python", "-u", "/run_verify.py"]
#CMD ["/usr/local/bin/verifyBamID", "-h"]

