FROM python:3

RUN git clone https://github.com/cpfair/tapiriik.git

WORKDIR /tapiriik

RUN pip3 install -r requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
	netcat \
	&& rm -rf /var/lib/apt/lists/*

ADD local_settings.py tapiriik/local_settings.py
ADD sync_worker.sh sync_scheduler.sh web.sh credentialstore_keygen_hex.py ./
