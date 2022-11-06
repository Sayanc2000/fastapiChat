FROM python:3.9.13

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload", "--ws-ping-timeout", "3600.0", "--ws-ping-interval", "20.0"]