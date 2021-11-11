FROM debian:latest
MAINTAINER Josh Anderson <joshand@cisco.com>

# You can provide comments in Dockerfiles
# Install any needed packages for your application
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    mercurial \
    wget \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 5000

COPY ["app.py", "requirements.txt", "/root/"]
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install -r /root/requirements.txt
RUN chmod +x /root/app.py
CMD ["/root/app.py"]
