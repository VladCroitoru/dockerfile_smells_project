FROM python:alpine3.8
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install numpy pandas
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "demo.py" ]