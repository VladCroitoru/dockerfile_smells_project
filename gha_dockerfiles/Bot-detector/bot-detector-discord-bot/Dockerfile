FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt install git -y

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD ["python3", "main.py"]
