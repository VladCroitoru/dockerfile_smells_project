FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y \
        git-core \
	python \
	python-openssl && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir /opt/headphones && \
    git clone https://github.com/rembo10/headphones.git /opt/headphones && \
    apt-get clean -y

EXPOSE 8282

VOLUME /mnt/media/music

CMD ["python", "/opt/headphones/Headphones.py", "--host=0.0.0.0", "--port=8282", "--datadir=/mnt/config/headphones", "--nolaunch"]
