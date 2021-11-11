FROM python:2.7
#ENV http_proxy 'http://192.168.8.7:3128'
#ENV https_proxy 'http://192.168.8.7:3128'
#ENV HTTP_PROXY 'http://192.168.8.7:3128'
#ENV HTTPS_PROXY 'http://192.168.8.7:3128'
ENV PYTHONUNBUFFERED 1
RUN mkdir /samp1
WORKDIR /samp1
COPY requirements.txt /samp1/
COPY . /samp1
RUN pip --default-timeout=60 install -r requirements.txt && python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
