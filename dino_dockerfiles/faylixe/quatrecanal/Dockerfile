FROM python:2.7-alpine
MAINTAINER Faylixe "felix.voituret@gmail.com"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY quatrecanal.py .

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["quatrecanal.py"]
