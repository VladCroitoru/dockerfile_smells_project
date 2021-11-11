FROM python:3.8

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install ./models/en_core_web_md-3.0.0.tar.gz

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--workers=2", "--threads=2", "app:app"]