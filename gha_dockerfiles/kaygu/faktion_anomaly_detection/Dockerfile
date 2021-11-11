FROM python:3.9-slim-buster

RUN mkdir /app
COPY . /app

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "--server.port $PORT"]
CMD ["app.py"]