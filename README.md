# Project Name

Short description or introduction to your project.

## Tech Stack

- Python
- FastAPI
- MongoDB

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install dependencies:

4. Set up environment variables (if applicable):

5. Run the application:

## API Routes

### Route 1: /api/objective1

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

### Route 2: /api/month/billing-data/

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:
  GET /api/month/billing?month=05-2023&company=623a020283ecc98fe0bf34e2

- Example Response:
  {
  "key": "value",
  ...
  }
