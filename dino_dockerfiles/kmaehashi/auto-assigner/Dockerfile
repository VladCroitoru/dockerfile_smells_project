FROM python:3.6-slim

RUN pip install pygithub
COPY auto_assigner.py /
ENTRYPOINT ["/auto_assigner.py"]
