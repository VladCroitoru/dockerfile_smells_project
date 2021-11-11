FROM python:3.8

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 5000

CMD [ "python", "main.py","runserver" ]