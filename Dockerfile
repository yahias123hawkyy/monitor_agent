FROM python:3

COPY monitor.py /app/monitor.py
RUN pip install docker

WORKDIR /app

CMD ["python", "monitor.py"]
