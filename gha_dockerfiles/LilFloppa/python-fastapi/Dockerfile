FROM python:3.9.7-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]