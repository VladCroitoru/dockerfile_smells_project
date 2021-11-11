FROM python:3
ADD carvalue_api.py /
ADD python_package_requirements.txt /
ADD web_1_model.p /
ADD labelencoder.p /
RUN pip3 install --no-cache-dir -r python_package_requirements.txt
CMD [ "python", "./carvalue_api.py" ]
