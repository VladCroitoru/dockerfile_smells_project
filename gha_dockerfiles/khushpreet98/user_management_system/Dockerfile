FROM python:3.9.5
COPY . /user_management_system
WORKDIR /user_management_system
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "manage.py seed_db" ]
CMD [ "main.py" ]
