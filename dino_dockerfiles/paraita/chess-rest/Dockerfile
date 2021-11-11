FROM python:3
MAINTAINER WOHLER Paraita <paraita.wohler@activeeon.com>

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sh", "-c", "./main.py"]