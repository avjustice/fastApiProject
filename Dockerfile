FROM python:3
RUN mkdir /code

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "update_currency_info.py"]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
