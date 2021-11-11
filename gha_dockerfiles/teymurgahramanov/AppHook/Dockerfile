FROM python:3.8.5
RUN mkdir /apphook
WORKDIR /apphook
RUN mkdir ssh
COPY ssh ./ssh
COPY apphook.py apphook.yml requirements.txt ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["apphook.py"]
