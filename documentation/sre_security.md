# Site Reliability Engineering and Security

## Logging

The API records operational events in:
network_api.log

## Input Validation

The API checks required fields before accepting new devices.

## Environment Variables

Sensitive credentials are stored in .env instead of Python source code.

## Authentication

The login endpoint verifies user credentials securely.

## Error Handling

Invalid API requests return meaningful HTTP responses.

## Reliability

Logging and validation improve monitoring and reduce configuration errors.