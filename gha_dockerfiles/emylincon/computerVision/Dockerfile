FROM python:3.7

WORKDIR app

COPY . .

RUN apt update -y && apt install -y \
    cmake \
    beep \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgirepository1.0-dev \
    && pip install -r requirements.txt \
    && pip install pygobject

CMD ["python3", "FrogGame.py"]