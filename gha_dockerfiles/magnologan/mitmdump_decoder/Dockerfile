FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8888

CMD [ "/usr/local/bin/mitmdump", "-p", "8888", "--no-http2", "-s", "decode.py", "--ignore", "^(?!pgorelease.nianticlabs.com)"]
