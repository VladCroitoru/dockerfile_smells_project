
FROM alpine:3.3

RUN apk --no-cache add py-pip libpq python-dev curl

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD / /app

WORKDIR /app

HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1

CMD python app.py & python admin.py
