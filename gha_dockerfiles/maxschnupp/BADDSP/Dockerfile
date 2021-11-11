FROM tensorflow/tensorflow:latest
WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends libsndfile1 ffmpeg
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD /app /app
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/serviceKey.json"