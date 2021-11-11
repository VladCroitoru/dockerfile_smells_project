FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN chmod +x ./runserver.sh
RUN chmod +x ./run_tests.sh
EXPOSE 8000