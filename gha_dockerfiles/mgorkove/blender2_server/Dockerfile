FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-runtime

COPY . .

RUN pip install -r requirements.txt

RUN python setup.py develop

CMD python parlai/chat_service/services/browser_chat/run.py --config-path parlai/chat_service/services/browser_chat/config.yml --port 8000
