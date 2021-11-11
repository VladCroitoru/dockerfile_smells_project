# Dockerfile, Image, Container

FROM python:3.7

RUN mkdir /usr/src/kirill_test_task

COPY . /usr/src/kirill_test_task

WORKDIR /usr/src/kirill_test_task

RUN pip install -r requirements.txt

EXPOSE 3000

ENTRYPOINT ["python", "manage.py"]
CMD ["makemigrations"]
CMD ["migrate"]
CMD ["runserver", "0.0.0.0:8000"]
