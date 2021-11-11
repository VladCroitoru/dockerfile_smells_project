FROM chapeter/chronic_docker:latest
MAINTAINER Josh Anderson <joshand@cisco.com>

# You can provide comments in Dockerfiles
# Install any needed packages for your application
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    libxml2-dev \
    libxslt-dev \
    mercurial \
    python-lxml \
    wget \
 && rm -rf /var/lib/apt/lists/*

COPY ["app.py", "requirements.txt", "/root/"]
RUN pip3 install -r /root/requirements.txt
RUN chmod +x /root/app.py
CMD ["python3", "-u", "/root/app.py"]
