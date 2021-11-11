FROM python:3
ADD my_script.py /
RUN easy_install pip
RUN pip install flask
RUN pip install flask_restful
CMD [ "python", "./my_script.py" ]