FROM python:2.7.12

RUN pip install fluent-logger

COPY script.py /tmp/script.py
RUN chmod +x /tmp/script.py

ENTRYPOINT [ "/tmp/script.py" ]
