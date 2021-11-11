FROM stockflare/base

# Install the latest AWS cli - needed for S3 command line actions in scripts
RUN apt-get update -y
RUN apt-get install -y python-pip
RUN pip install awscli

CMD ['puma']
