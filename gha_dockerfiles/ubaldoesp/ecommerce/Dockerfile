FROM python:3.7

ENV PYTHONUNBUFFERED 1 
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /ecommerce
WORKDIR /ecommerce

COPY requirements.txt /ecommerce/
RUN pip install -r requirements.txt

CMD python manage.py  runserver 0.0.0.0:8000