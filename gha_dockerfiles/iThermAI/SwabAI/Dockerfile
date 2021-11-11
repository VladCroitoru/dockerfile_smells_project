FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY config/requirements.txt /tmp/

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential cmake && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . .

CMD [ "python3", "main.py" ]
