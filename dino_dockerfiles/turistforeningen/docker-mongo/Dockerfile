from mongo:3

VOLUME ["/app", "/secrets"]

COPY setup.sh /setup.sh
RUN chmod +x setup.sh

RUN apt-get update && apt-get install -y --no-install-recommends python-pip
RUN pip install awscli
