FROM python:3
WORKDIR /code
ADD . /code

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "run.py"]
