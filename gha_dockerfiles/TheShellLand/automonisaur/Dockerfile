# pypi requirements
FROM python:3 as builder
RUN python3 -m pip install --upgrade pip setuptools wheel twine
RUN apt update && apt install -y vim
COPY requirements.txt .
RUN pip install -U -r requirements.txt


FROM builder as runner
LABEL maintainer="naisanza@gmail.com"
LABEL description="automonisaur core library"

WORKDIR /automonisaur

COPY automon automon
COPY README.md .
COPY LICENSE .
COPY entry.sh .
COPY unittests.sh .
COPY setup.py .

CMD ["/bin/bash"]
ENTRYPOINT ["/bin/bash", "entry.sh"]