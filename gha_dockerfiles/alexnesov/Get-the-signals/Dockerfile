FROM python:3.8.0-slim
LABEL maintainer alexandrenesovic@gmail.com

ARG aws_db_endpoint
ARG aws_db_pass
ARG aws_db_user

ENV aws_db_endpoint=$aws_db_endpoint
ENV aws_db_pass=$aws_db_pass
ENV aws_db_user=$aws_db_user

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt
COPY . /app

ENV FLASK_ENV development
EXPOSE 5000
CMD ["python","app.py"]
