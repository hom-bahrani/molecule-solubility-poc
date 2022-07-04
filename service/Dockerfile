FROM python:3.9-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

RUN mkdir -p /model

ENV TIMEOUT=300

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
