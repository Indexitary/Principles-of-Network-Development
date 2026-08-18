# Network Device API Testing Results

This document records REST API GET requests and responses completed using Postman.

The API represents the enterprise network created in Lab 3.

## GET - Retrieve Home Devices

Endpoint: http://127.0.0.1:5000/home/devices
Method: GET
Purpose: Retrieve network device information from the REST API.
Result: API unavailable because the REST API has not yet been implemented.
Observed Error: Connection refused - no service running on port 5000.
Future Development: The REST API will be implemented in lab 6 using Python and Flask.

## GET - Retrieve Specific Home Routers

Endpoint: http://127.0.0.1:5000/home/routers/R1
Method: GET
Purpose: Retrieve router information from the REST API.
Result: API unavailable because the REST API has not yet been implemented.
Observed Error: Connection refused - no service running on port 5000.
Future Development: The REST API will be implemented in lab 6 using Python and Flask.

## GET - Retrieve Home Switches

Endpoint: http://127.0.0.1:5000/home/switches
Method: GET
Purpose: Retrieve switch information from the REST API.
Result: API unavailable because the REST API has not yet been implemented.
Observed Error: Connection refused - no service running on port 5000.
Future Development: The REST API will be implemented in lab 6 using Python and Flask.

## GET - Retrieve Cloud Servers

Endpoint: http://127.0.0.1:5000/servers
Method: GET
Purpose: Retrieve cloud servers information from the REST API.
Result: API unavailable because the REST API has not yet been implemented.
Observed Error: Connection refused - no service running on port 5000.
Future Development: The REST API will be implemented in lab 6 using Python and Flask.

# API Troubleshooting Expected Results

This section records REST API testing activities, errors identified and solutions applied.

## Expected Successful API Request

Resource: /home/routers/R1
Method: GET
Expected Status: 200 OK
Purpose: Retrieve router information from the Network Device Management API.
Implementation: The API will be developed during Lab 6.

## 400 Bad Request

Problem: Invalid JSON syntax.
Solution: Corrected the request format.

## 404 Not Found

Problem: Request network device doe snot exist.
Solution: Verified the device hostname and endpoint.

## 401 Unauthorized

Problem: Request attempted without valid authentication.
Concept: API requires identity verification before allowing access.

## 403 Forbidden

Problem: User does not have permission to access the resource.
Concept: Access permissions control resource availability.

## 500 Internal Server Error

Problem: Server-side failure.
Solution: Investigate API service and backend systems.

## API Headers

Header: Content-Type: application/json
Purpose: Defines the format of exchanged data.

## Webhook Example Testing

Event: Router status changed.
Purpose: Automatically notify another system about network events.