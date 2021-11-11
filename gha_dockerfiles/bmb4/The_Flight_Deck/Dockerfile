FROM python:3.9
ENV HOME /root
WORKDIR /root
COPY . .
#Didn't run here either but got a different error, on import pymongo in main.py
#RUN python -m pip install 'pymongo[srv]'

# heroku[web.1]: Starting process with command `/bin/sh -c python3\ main.py\ \8290`
# heroku[web.1]: Process exited with status 1
# app[web.1]: Traceback (most recent call last):
# app[web.1]:   File "/root/main.py", line 5, in <module>
# app[web.1]:     import pymongo
# app[web.1]: ModuleNotFoundError: No module named 'pymongo'
# heroku[web.1]: State changed from starting to crashed

RUN pip install -r requirements.txt
EXPOSE $PORT

CMD python3 main.py $PORT

