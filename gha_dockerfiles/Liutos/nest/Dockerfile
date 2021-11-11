FROM python:3.8

# Set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/ShangHai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -i 'https://pypi.tuna.tsinghua.edu.cn/simple' -r requirements.txt
RUN pip3 install -i 'https://pypi.tuna.tsinghua.edu.cn/simple' uwsgi

COPY . .

CMD ["honcho", "start", "web"]
