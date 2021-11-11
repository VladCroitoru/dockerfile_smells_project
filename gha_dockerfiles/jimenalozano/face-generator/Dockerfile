FROM tensorflow/tensorflow:1.14.0-gpu-py3
WORKDIR /face-generator
COPY . /face-generator
RUN pip install -r requirements.txt
RUN python cli.py
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "--timeout", "4800", "face_generator:app"]
