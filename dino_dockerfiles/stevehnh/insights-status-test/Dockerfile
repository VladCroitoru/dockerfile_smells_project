FROM debian
MAINTAINER Stephen Adams <sadams@redhat.com>
RUN apt-get update -y && apt-get upgrade -y && apt-get install jq curl python python-pip -y && apt-get clean
RUN pip install requests
COPY request-status.py /usr/bin/request-status.py
CMD ["python", "/usr/bin/request-status.py"]
