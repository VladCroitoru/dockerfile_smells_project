FROM python:3.8
WORKDIR /app
COPY src/requirements.txt .
RUN python -m pip install -r requirements.txt
COPY src/. .
EXPOSE 5000
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:5000"]