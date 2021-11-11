FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /api
COPY /src/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY /src .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]