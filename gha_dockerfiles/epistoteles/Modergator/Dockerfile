FROM python:3.8
WORKDIR /modergator
COPY . .
RUN apt-get update && apt-get install -y screen net-tools tesseract-ocr virtualenv ffmpeg
RUN chmod +x install.sh
RUN chmod +x run.sh
RUN pip3 install virtualenv
CMD ["./run.sh", ";", "sleep", "10", ";", "screen", "-r", "telegram-bot"]