FROM python:3.7-alpine
ENV PYTHON_UNBUFFERED 1
RUN pip install requests
ADD cli.py /
ENTRYPOINT ["python", "/cli.py"]
