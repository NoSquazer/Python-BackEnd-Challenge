# Project Name

Python Backend Challenge

## Tech Stack

- Python
- FastAPI
- MongoDB

## Installation

1. Clone the repository:
   git clone [https://github.com/NoSquazer/Python-BackEnd-Challenge.git]

2. Navigate to the project directory:
   cd your-repo-name

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

## API Routes

### Route 1: /api/month/resume

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:
  GET /api/month/resume?month=05-2023&company=623a020283ecc98fe0bf34e2

- Example Response:
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

### Route 2: /api/month/billing

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:
  GET /api/month/billing?month=05-2023&company=623a020283ecc98fe0bf34e2

- Example Response:
  [
  {
  "day": "0",
  "altas_count": "0",
  "recurrency_count": "0"
  }
  ]

### Route 3: /api/month/billing-summary

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:
  GET /api/month/billing-summary?month=05-2023&company=623a020283ecc98fe0bf34e2

- Example Response:
  {
  "total_revenue_current": 0,
  "total_revenue_variation": 0,
  "recurrences_revenue_current": 0,
  "recurrences_revenue_variation": 0,
  "altas_revenue_current": 0,
  "altas_revenue_variation": 0
  }

### Route 4: /api/month/porcentage-metrics

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:
  GET /api/month/porcentage-metrics?month=05-2023&company=623a020283ecc98fe0bf34e2

- Example Response:
  {
  "recurring_charges": 0,
  "checkout": 0,
  "checkout_miclub": 0,
  "recurring_miclub": 0,
  "local_level": 0,
  "plus_level": 0,
  "total_level": 0
  }
