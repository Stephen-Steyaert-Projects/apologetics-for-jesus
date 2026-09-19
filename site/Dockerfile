FROM python:3.14-alpine AS build

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files and install dependencies (cached until these change)
COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-dev --no-install-project --group prod

# Copy application code and install the project itself
COPY . .
RUN uv sync --frozen --no-dev --group prod

# Minify CSS
RUN uv run --with rcssmin python3 -c "\
import rcssmin, pathlib; \
[pathlib.Path(p.parent / (p.stem + '.min.css')).write_text(rcssmin.cssmin(p.read_text())) \
 for p in [ \
	pathlib.Path('src/apologetics_for_jesus/static/css/base.css'), \
	pathlib.Path('src/apologetics_for_jesus/static/css/gospel/base.css'), \
 ]]"

# Production stage
FROM python:3.14-alpine

WORKDIR /app

# Copy virtual environment and app from build stage
COPY --from=build /app/.venv /app/.venv
COPY --from=build /app /app

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Expose gunicorn port
EXPOSE 8000

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--worker-class", "sync", "apologetics_for_jesus:app"]
