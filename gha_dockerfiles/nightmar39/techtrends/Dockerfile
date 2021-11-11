FROM python:2.7 
COPY /techtrends /web
WORKDIR /web
RUN pip install -r requirements.txt
RUN python init_db.py
EXPOSE 3111/tcp
ENTRYPOINT ["python"]
CMD ["app.py"]
