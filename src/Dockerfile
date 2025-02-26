FROM python:3.12.3
EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY . /app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.py"]