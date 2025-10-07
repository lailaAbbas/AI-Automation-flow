FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3002
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "3002"]
