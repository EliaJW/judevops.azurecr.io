# Välj en basbild som har Python installerat
FROM python:3.12-slim

# Ställ in arbetskatalogen i containern

# Kopiera requirements.txt till arbetskatalogen
COPY . .

# Installera Python-beroenden
RUN pip install -r requirements.txt

# Kopiera applikationsfilerna till arbetskatalogen

# Specificera hur applikationen ska köras när containern startas
ENTRYPOINT ["python", "/calculator.py"]