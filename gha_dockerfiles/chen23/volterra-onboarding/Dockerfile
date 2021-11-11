FROM python:3

WORKDIR /usr/src/app

ENV IN_DOCKER YES

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x cli.py

ENTRYPOINT [ "python", "./cli.py" ]