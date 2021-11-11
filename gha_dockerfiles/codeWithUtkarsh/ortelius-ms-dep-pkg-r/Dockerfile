FROM quay.io/ortelius/ms-python-base:flask-1.1
ENV PYTHONUNBUFFERED=1
WORKDIR /code/
ADD requirements.txt /code/
RUN pip install -r requirements.txt && python -m pip uninstall -y pip;
ADD . /code
EXPOSE 5000
CMD ["python", "main.py"]
