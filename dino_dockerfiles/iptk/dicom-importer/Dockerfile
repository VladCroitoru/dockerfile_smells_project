FROM python:3.6-alpine

VOLUME /storage
VOLUME /nps/datasets

RUN pip3 install pydicom
ADD import.py /import.py

CMD ["python3", "/import.py"]