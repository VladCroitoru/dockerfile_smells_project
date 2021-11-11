FROM python:3.9-slim
WORKDIR /home
COPY ./requirements.txt .
RUN pip install --no-cache-dir --requirement requirements.txt
COPY ./exporter.py .
CMD ["python", "./exporter.py"]
