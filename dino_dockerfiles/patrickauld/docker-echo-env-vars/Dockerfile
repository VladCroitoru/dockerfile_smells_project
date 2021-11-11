FROM python:3-slim
MAINTAINER Patrick Auld "patrick@patrickauld.com"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]