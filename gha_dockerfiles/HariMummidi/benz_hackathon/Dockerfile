FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

