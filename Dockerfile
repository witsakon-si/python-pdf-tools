FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY packages.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r packages.txt

COPY main.py /app/
COPY views /app/

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
