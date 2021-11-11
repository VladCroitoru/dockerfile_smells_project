
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app/requirements.txt /app/

RUN pip3 install -r requirements.txt 

COPY ./app/preprocessor.py /app/
COPY ./app/training /app/training 
COPY ./app/models /app/models

RUN python training/train_spam_detector_MLPClassifier.py
RUN python training/train_spam_detector_KNeighborsClassifier.py
RUN python training/train_spam_detector_DecisionTreeClassifier.py
RUN python training/train_spam_detector_RandomForestClassifier.py

COPY ./app /app

WORKDIR /app