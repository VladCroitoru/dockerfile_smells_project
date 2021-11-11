FROM python:2.7.11

RUN apt-get update && \
    apt-get install -y iceweasel && \
    apt-get install -y python-pip && \
    apt-get install -y xvfb

RUN pip install -U pyvirtualdisplay selenium toml

RUN useradd -m selenium
USER selenium

ADD entrypoint.sh .
ADD main.py .
ENTRYPOINT ["./entrypoint.sh"]
