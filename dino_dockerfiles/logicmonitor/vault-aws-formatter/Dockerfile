FROM python:2.7-slim

RUN pip install argparse

COPY vault_aws_formatter.py /usr/local/bin

ENTRYPOINT [ "python", "/usr/local/bin/vault_aws_formatter.py" ]
