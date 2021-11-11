FROM python:3.8.5

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY *.py /app/
ENTRYPOINT ["python", "/app/walls.py"]
