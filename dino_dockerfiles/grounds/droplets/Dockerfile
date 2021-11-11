FROM ubuntu:14.04

# Install dependencies
RUN apt-get update -q && \
    apt-get install -y \
    unzip \
    wget

# Install packer
RUN cd ~/ && \
    mkdir packer && \
    cd packer && \
    wget https://dl.bintray.com/mitchellh/packer/0.7.1_linux_386.zip && \
    unzip 0.7.1_linux_386.zip

# Add packer to path    
ENV PATH $PATH:~/packer/

# Copy project files
COPY . /droplets

# Set the final working dir to the project directory
WORKDIR /droplets

# Default droplet region
ENV REGION Amsterdam 3

# Default droplet size
ENV SIZE 512MB

# Default droplet prefix
ENV SIZE grounds

ENTRYPOINT ["/packer/packer-packer", "-var-file=images/variables.json"]
