FROM ubuntu:16.04
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8
RUN apt-get update ; apt-get install -y  ca-certificates python3 python3-urllib3 python3-flask ; apt-get clean
ADD app.py /
Add templates /templates
CMD ["python3", "app.py"]
