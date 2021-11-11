FROM python:2.7-alpine
ENV PYTHON_UNBUFFERED 1
RUN pip install requests
ADD . /app/
ENTRYPOINT ["python", "/app/service.py"]
