FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
	sudo \
	wget \
	vim \
	zip \
	unzip

# root権限意外でも扱えるようにする 共有サーバとか
WORKDIR /opt

# Anaconda3 任意のversionをinstall
RUN wget https://repo.continuum.io/archive/Anaconda3-2021.05-Linux-x86_64.sh && \
	sh Anaconda3-2021.05-Linux-x86_64.sh -b -p /opt/anaconda3 && \
	# インストール後必要ないから削除
	rm -f Anaconda3-2021.05-Linux-x86_64.sh

# aws CLI: https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-linux.html
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

ENV PATH /opt/anaconda3/bin:$PATH
RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

WORKDIR /
  CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
