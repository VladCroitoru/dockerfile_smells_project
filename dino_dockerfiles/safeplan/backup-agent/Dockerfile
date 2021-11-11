FROM python:3.6
# note: if you move to python 3.7, async is a keyword and its used as a property name in the the safeplan api (and so it will fail).

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    libssl-dev \
    openssl \
    libacl1-dev \
    libacl1 \
    build-essential \
    libfuse-dev \
    fuse \
    pkg-config 

# install nfs server 
#RUN echo exit 0 > /usr/sbin/policy-rc.d
#RUN mkdir /nfs
#RUN mkdir /run/sendsigs.omit.d # required for starting rpcbind
#RUN apt install -y nfs-kernel-server
#RUN echo "/nfs *(rw,fsid=0,sync,insecure)" > /etc/exports

RUN rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir borgbackup==1.1.10 llfuse
RUN echo "user_allow_other" >> /etc/fuse.conf

VOLUME ["/var/safeplan/backup" , "/var/safeplan/config", "/var/safeplan/repo", "/var/safeplan/work", "/root/.ssh" , "/var/safeplan/history"]

ENV SAFEPLAN_ID NOT_SET
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY api /usr/src/app

EXPOSE 8080
ENV TZ=Europe/Vienna
ENV BORG_RSH="ssh -o BatchMode=yes -o ServerAliveInterval=10 -o ServerAliveCountMax=30"
ENV BORG_MOUNT_DATA_CACHE_ENTRIES="10"

ENTRYPOINT ["python3"]

CMD ["app.py"]