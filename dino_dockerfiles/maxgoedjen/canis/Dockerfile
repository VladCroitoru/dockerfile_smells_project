FROM python:3.5.1
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python application.py