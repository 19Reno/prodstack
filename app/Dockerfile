# Stage 1 — build stage
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2 — final stage
FROM python:3.11-slim

# Create non-root user — never run apps as root
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

# Copy only installed packages from builder stage
COPY --from=builder /root/.local /home/appuser/.local

# Copy app code
COPY app.py .

# Set ownership
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Tell Docker this container listens on port 5000
EXPOSE 5000

# Set PATH so Python finds the packages
ENV PATH=/home/appuser/.local/bin:$PATH

# Start the app
CMD ["python", "app.py"]
