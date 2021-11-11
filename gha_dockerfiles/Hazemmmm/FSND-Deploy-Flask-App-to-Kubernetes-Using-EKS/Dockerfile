FROM python:stretch

COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY ./ app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask 

ENTRYPOINT ["gunicorn", "-b", ":8080", "main:APP"]