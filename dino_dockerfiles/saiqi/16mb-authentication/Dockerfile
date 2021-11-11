FROM python:3.6-alpine
RUN mkdir /service
ADD ./requirements.txt /service
WORKDIR /service
RUN pip install -r requirements.txt
COPY application /service/application
EXPOSE 5000
CMD ["gunicorn","-b",":5000","application.app:app"]