FROM ubuntu:latest

# Install dependencies (1)
RUN apt-get update
RUN apt-get -y install apt-transport-https ca-certificates curl --no-install-recommends

# Add repo and key
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list

# Install chrome and bibtexparser
RUN apt-get update
RUN apt-get install -y google-chrome-stable python wget python-pip python-setuptools --no-install-recommends
RUN pip install -U pip && \
    pip install bibtexparser

# Add chrome user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome/Downloads

# Add executable
ADD bibtex2pdf.py /home/chrome/bibtex2pdf.py

# Add Downloads folder
RUN mkdir -p /home/chrome/bibtex-downloads
RUN chown -R chrome:chrome /home/chrome

# Clean
RUN apt-get purge --auto-remove -y curl && rm -rf /var/lib/apt/lists/*
