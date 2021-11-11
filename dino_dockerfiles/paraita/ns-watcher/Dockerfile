FROM python:3
MAINTAINER WOHLER Paraita <paraita.wohler@gmail.com>

WORKDIR /root
COPY nswatcher nswatcher
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "-m", "nswatcher.main"]