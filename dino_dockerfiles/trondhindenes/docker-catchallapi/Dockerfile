FROM python:3
MAINTAINER trond
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN mv /app/config-prod.yml /app/config.yml
ENV PYTHONUNBUFFERED=1
EXPOSE 80
ENTRYPOINT ["python"]
CMD ["web.py"]
