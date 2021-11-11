FROM python:2.7-alpine
COPY * /src/
EXPOSE 53
CMD ["python", "/src/dnsproxy.py", "-s 8.8.8.8"]
