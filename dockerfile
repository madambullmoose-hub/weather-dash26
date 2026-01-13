FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 7860
# Hugging Face needs host 0.0.0.0 and port 7860
CMD ["python", "main.py"]
