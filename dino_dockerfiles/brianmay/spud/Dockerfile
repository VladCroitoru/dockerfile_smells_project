# Start with a Python image.
FROM python:3.8-buster
LABEL maintainer="Brian May <brian@linuxpenguins.xyz>"

# Some stuff that everyone has been copy-pasting
# since the dawn of time.
ENV PYTHONUNBUFFERED 1

# Install OS dependencies
RUN apt-get update \
 && apt-get install -y \
    sudo \
    libimage-exiftool-perl ffmpeg exiftran \
    dcraw \
 && rm -rf /var/lib/apt/lists/*

# Make application directory
RUN mkdir -p /opt/spud /etc/spud
WORKDIR /opt/spud

# Install our requirements.
RUN pip install pipenv
ADD Pipfile Pipfile.lock /opt/spud/
RUN pipenv install --system --deploy

# Copy all our files into the image.
COPY . /opt/spud/

RUN find -type d -print0 | xargs -0 chmod 755 \
 && find -type f -print0 | xargs -0 chmod 644 \
 && find scripts -type f -name "*.sh" -print0 | xargs -0 chmod 755 \
 && chmod 755 *.py \
 && chmod 644 conftest.py

# Setup access to version information
ARG BUILD_DATE=
ARG VCS_REF=
ENV BUILD_DATE=${BUILD_DATE}
ENV VCS_REF=${VCS_REF}

# Specify the command to run when the image is run.
EXPOSE 8000
VOLUME '/etc/spud' '/var/lib/spud'
CMD /opt/spud/scripts/docker.sh
