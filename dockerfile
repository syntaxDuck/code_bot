FROM python

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src .
CMD ["python", "main.py"]
