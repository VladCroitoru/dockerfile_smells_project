FROM python:3.6-alpine
RUN pip install elasticsearch iptk==0.6
COPY index.py /index.py
CMD ["python3", "/index.py"]