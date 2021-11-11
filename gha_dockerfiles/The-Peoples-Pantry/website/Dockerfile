FROM python:3.9
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
ENV DEBUG=True
ENV DJANGO_SUPERUSER_PASSWORD=password
ENV PORT=8000
EXPOSE ${PORT}
RUN python website/manage.py migrate
RUN python website/manage.py createsuperuser --no-input --username user@example.com --email user@example.com
ENTRYPOINT ["python", "website/manage.py", "runserver", "0.0.0.0:8000"]
