FROM python:3.6

WORKDIR /exporter
ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD exporter.py ./

ENTRYPOINT ["python", "exporter.py"]
CMD ["--target", "www.oxalide.com", "--icmp", "--tcp", "80", "443" ]
