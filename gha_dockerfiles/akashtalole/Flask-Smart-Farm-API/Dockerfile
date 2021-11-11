FROM python:3.9.1
ADD . /flask-smart-farm
WORKDIR /flask-smart-farm
RUN pip install -r requirements.txt
ENV PORT 5000
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "manage.py" ]