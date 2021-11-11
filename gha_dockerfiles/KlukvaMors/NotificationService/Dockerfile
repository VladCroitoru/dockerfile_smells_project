FROM python:3.8

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app
COPY . /usr/src/app/

EXPOSE 8080
RUN pip install --no-cache-dir -r requirements.txt

ENV AUTH_USERNAME=
ENV AUTH_PASSWORD=
ENV SMTP_HOST=
ENV SMTP_PORT=
ENV SMTP_USERNAME=
ENV SMTP_PASSWORD=
ENV TO_EMAIL=

CMD ["python", "app.py"]
