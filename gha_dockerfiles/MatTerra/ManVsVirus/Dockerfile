FROM python:3.7.7
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN rm requirements.txt
ADD backend .
EXPOSE 8080
RUN export PYTHONPATH=$PYTHONPATH:/
WORKDIR /
CMD ["uwsgi", "--ini", "/backend/wsgi.ini"]
