# API

## About

API - Python Backend Challenge

Technologies used:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [MongdoDB](https://www.mongodb.com/)

## Installation

```bash
git clone https://github.com/NoSquazer/Python-BackEnd-Challenge.git
```

### Create .env file

```bash
cp .env.example .env
```

### Instrall requirements

```bash
pip install -r requirements/requirements.txt
```

### Setup for local development

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Routes

### Route 1: /api/month/resume

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:

```bash
  GET /api/month/resume?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  {
  "active_clients": 98,
  "active_members_porcentage_change_prev_month": 3,
  "new_clients": 107,
  "new_clients_porcentage_change_prev_month": -16,
  "deregistrations": 84,
  "deregistrations_porcentage_change_prev_month": -34,
  "inactivations_without_termination": 193,
  "inactivations_without_termination_porcentage_change_prev_month": -11
  }
```

### Route 2: /api/month/billing

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:

```bash
  GET /api/month/billing?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  [
  {
  "day": "0",
  "altas_count": "0",
  "recurrency_count": "0"
  }
  ]
```

### Route 3: /api/month/billing-summary

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business identifier.

- Example Request:

```bash
  GET /api/month/billing-summary?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  {
  "total_revenue_current": 0,
  "total_revenue_variation": 0,
  "recurrences_revenue_current": 0,
  "recurrences_revenue_variation": 0,
  "altas_revenue_current": 0,
  "altas_revenue_variation": 0
  }
```

### Route 4: /api/month/porcentage-metrics

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:

```bash
  GET /api/month/porcentage-metrics?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  {
  "recurring_charges": 0,
  "checkout": 0,
  "checkout_miclub": 0,
  "recurring_miclub": 0,
  "local_level": 0,
  "plus_level": 0,
  "total_level": 0
  }
```
