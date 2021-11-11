FROM python:3.8.5

COPY /static/AnimatedSticker.tgs /static/AnimatedSticker.tgs
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY covid.py .
COPY main.py .
COPY wearher.py .
CMD [ "python", "./main.py" ]
