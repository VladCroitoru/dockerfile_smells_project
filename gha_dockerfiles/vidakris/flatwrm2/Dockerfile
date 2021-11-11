FROM tensorflow/tensorflow:2.3.4-gpu-jupyter
COPY requirements.txt /tmp/
USER root
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt #&& \
    fix-permissions "/home/${NB_USER}"
WORKDIR /app
COPY . .
RUN python setup.py install 
CMD ps ax|grep python3 |while read -a i; do kill $i; done
CMD "bash" "-c" "source /etc/bash.bashrc && jupyter notebook --notebook-dir=/app --ip 0.0.0.0 --no-browser --allow-root"
