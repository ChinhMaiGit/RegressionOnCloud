# Use official Python image
FROM python:3.13-slim 

# Install uv 
COPY --from=ghcr.io/astral-sh/uv:0.4.0 /uv /usr/local/bin/uv 

# Set working directory
WORKDIR /app 

# Copy project files
COPY pyproject.toml .  
COPY uv.lock . 

# Install dependencies with uv 
RUN uv sync --frozen --no-dev 

# Copy the rest of the files
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]