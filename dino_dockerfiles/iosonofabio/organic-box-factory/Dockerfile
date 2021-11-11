FROM finalduty/archlinux:latest
MAINTAINER Fabio Zanini <fabio DOT zanini AT stanford DOT edu>
# Configure image
COPY configure_image.sh /configure_image.sh
RUN /usr/bin/bash configure_image.sh
# Add pipeline to image
COPY pipeline/pipeline.py /usr/bin/pipeline
# Set ENTRYPOINT to run the Docker/Singularity image
#ENTRYPOINT /usr/bin/pipeline
