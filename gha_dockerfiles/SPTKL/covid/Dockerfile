FROM python:3.7-slim-stretch as build

WORKDIR /app

COPY . .

RUN python3 -m venv venv

RUN pip3 install --no-cache-dir -e . 

CMD [ "./entrypoint.sh" ]
