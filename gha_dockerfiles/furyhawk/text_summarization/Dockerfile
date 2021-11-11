FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
# CMD ["python", "./app/text_sum_endpoint.py"]
CMD ["uvicorn", "app.text_sum_endpoint:app", "--host", "0.0.0.0", "--port", "8000"]
