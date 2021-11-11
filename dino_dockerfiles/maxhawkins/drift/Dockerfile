FROM ubuntu:15.04

RUN DEBIAN_FRONTEND=noninteractive && \
	apt-get update && \
	apt-get install -y  \
		ffmpeg python-pip python-numpy \
		python-scipy python-pip && \
	apt-get clean

ADD . /drift

RUN cd /drift && pip install -r requirements.txt

VOLUME /drift/uploads
VOLUME /drift/db

EXPOSE 9876

CMD cd /drift && python serve.py \
	--db_path /drift/db/app.db \
	--blob_folder /drift/uploads
