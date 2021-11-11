FROM python:3.6-slim
WORKDIR /Song_Prediction
COPY requirements.txt /Song_Prediction/requirements.txt
RUN pip install -r requirements.txt

COPY . /Song_Prediction
ENTRYPOINT [ "python" ]
CMD ["WebUI.py"]
