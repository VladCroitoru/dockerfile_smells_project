FROM python:3.10.0a4-slim-buster
WORKDIR /app
COPY . .
RUN pip install -r hello-kube-py_req.txt
EXPOSE 3000
CMD ["python", "hello-kube.py"]
