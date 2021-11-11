FROM python:3

ADD /app /app
COPY Readme.md /app/Readme.md

EXPOSE 80 443

RUN pip install -r /app/requirements.txt

WORKDIR /app
ENTRYPOINT ["python", "./app.py"]
