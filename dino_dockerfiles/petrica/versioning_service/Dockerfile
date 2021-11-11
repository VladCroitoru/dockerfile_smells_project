FROM python:2.7

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x /app/run.sh
ENTRYPOINT ["/app/run.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]