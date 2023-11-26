# Vendor Management System (VMS)

Welcome to the Vendor Management System (VMS) project! This system helps manage vendors, purchase orders, and performance metrics.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Development Server](#running-the-development-server)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
  - [Running Tests](#running-tests)
- [Code Quality](#code-quality)
- [License](#license)

## Getting Started

### Prerequisites

- Python 4.2.2
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone [https://github.com/Siddiqui123321/vendor-mng-performance.git]
   cd vendor-mng-performance.git
Install dependencies:
pip install -r requirements.txt


## Usage

### Running the Development Server
Run the following command to start the development server:
python manage.py runserver
The server will be accessible at http://localhost:8000.

### API Endpoints
Vendor API: /api/vendors/
Purchase Order API: /api/purchase_orders/
Authentication API: /api/token/

## Testing
### Running Tests
To run the test suite, use the following command:
python manage.py test

## Code Quality
The project uses Flake8 for linting. You can check code quality by running:
flake8

License
This project is licensed under the MIT License - see the LICENSE file for details.
https://github.com/Siddiqui123321/vendor-mng-performance.git

## API Models

### Vendor
Represents a vendor with fields like name, contact_details, address, vendor_code, and performance metrics.

### PurchaseOrder
Represents a purchase order with fields like po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating, issue_date, and acknowledgment_date. Also includes methods for calculating performance metrics.

### HistoricalPerformance
Represents historical performance metrics for vendors. Includes fields like vendor, date, on_time_delivery_rate, quality_rating_avg, average_response_time, and fulfillment_rate.

## API Views

- **VendorListCreateView**: List and create vendors.
- **VendorRetrieveUpdateDeleteView**: Retrieve, update, or delete a vendor.
- **VendorPerformanceView**: Retrieve performance metrics for a vendor.
- **PurchaseOrderListCreateView**: List and create purchase orders with an option to filter by vendor.
- **PurchaseOrderRetrieveUpdateDeleteView**: Retrieve, update, or delete a purchase order.
- **AcknowledgePurchaseOrderView**: Acknowledge a purchase order, updating acknowledgment date and triggering response time recalculation.

## Signals

- **purchase_order_saved**: Signal handler for post-save actions on a PurchaseOrder, including metric calculations and historical performance creation.

## Django Settings

- **SECRET_KEY**: Django secret key for security (make sure to keep it secret).
- **DEBUG**: Debug mode (True for development, False for production).
- **ALLOWED_HOSTS**: List of allowed hosts in production.
- **INSTALLED_APPS**: List of installed Django apps.
- **MIDDLEWARE**: List of middleware classes.
- **DATABASES**: Database configuration (SQLite by default).
- **AUTH_PASSWORD_VALIDATORS**: Password validation settings.
- **LANGUAGE_CODE**: Default language for the project.
- **TIME_ZONE**: Default timezone for the project.
- **USE_I18N, USE_TZ**: Internationalization and timezone settings.
- **STATIC_URL**: URL to access static files.
- **DEFAULT_AUTO_FIELD**: Default primary key field type.
- **REST_FRAMEWORK**: Django REST Framework settings.
- **SIMPLE_JWT**: Simple JWT settings for token-based authentication.
