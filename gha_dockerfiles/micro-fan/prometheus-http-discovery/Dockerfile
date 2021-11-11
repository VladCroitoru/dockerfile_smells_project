FROM python:3.9.2-alpine3.13

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make \
    && pip install --no-cache-dir "uvicorn[standard]" \
    && apk del .build-deps gcc libc-dev make

COPY requirements.txt /home/
RUN pip3 install -r /home/requirements.txt

COPY ./app /app
WORKDIR /

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["app/main.py"]
ENTRYPOINT ["python3"]
