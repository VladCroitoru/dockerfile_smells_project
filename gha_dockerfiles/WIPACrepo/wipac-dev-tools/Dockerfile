FROM python:latest

COPY README.md requirements.txt setup.cfg setup.py /usr/src/wipac_dev_tools/
COPY wipac_dev_tools /usr/src/wipac_dev_tools/wipac_dev_tools
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /usr/src/wipac_dev_tools/requirements.txt

RUN useradd -m -U app
USER app

WORKDIR /usr/src/wipac_dev_tools
CMD ["python3", "-c", "print('Hello, wipac_dev_tools!')"]
