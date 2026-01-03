FROM python:3.11-slim AS base

WORKDIR /app

COPY app/ app/

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

EXPOSE 5000

CMD ["python", "app/main.py"]