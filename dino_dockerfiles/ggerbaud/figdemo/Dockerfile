FROM python:2.7
ADD requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . /code
CMD ["python", "app.py"]
