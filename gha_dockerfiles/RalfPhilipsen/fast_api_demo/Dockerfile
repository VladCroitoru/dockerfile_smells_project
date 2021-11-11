FROM python:3.8

COPY requirements.txt /home/ubuntu/fast_api_demo/
WORKDIR /home/ubuntu/fast_api_demo
RUN pip install -r requirements.txt

COPY . /home/ubuntu/fast_api_demo/

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--workers", "8", "--host", "0.0.0.0", "--port", "80", "--timeout-keep-alive", "600"]
