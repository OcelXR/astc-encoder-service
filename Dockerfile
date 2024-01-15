FROM python:latest

RUN pip install --no-cache-dir Flask

WORKDIR /app
COPY . /app

EXPOSE 3000
CMD python -m http.server 3000

CMD ["python", "app.py"]
