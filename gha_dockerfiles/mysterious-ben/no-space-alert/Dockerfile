FROM python:3.8.6-slim-buster
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app
COPY . /app
# RUN apt-get update && apt-get install build-essential -y
RUN \
  pip install pip -U \
  pip install --no-cache-dir -r requirements.txt
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "-m", "src.cli"]
CMD ["--help"]
