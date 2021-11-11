FROM index.alauda.cn/library/python:2
ADD pip.conf /root/.pip/pip.conf
RUN pip install tornado
RUN pip install requests
EXPOSE 80
COPY . /myweb/
WORKDIR /myweb/
CMD python getimage.py 
