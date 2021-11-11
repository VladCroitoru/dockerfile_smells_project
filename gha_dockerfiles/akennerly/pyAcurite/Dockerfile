FROM python:3.8.6-alpine3.12

LABEL maintainer="Andrew Kennerly <andrew@kennerly.net>"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY main.py /app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]
