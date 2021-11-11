FROM python:3.9.7-slim-bullseye
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000:5000
CMD [ "gunicorn", "-b 0.0.0.0:5000", "--workers=4", "api:app" ]
