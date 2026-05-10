---
name: api-documenter
description: Generate comprehensive API documentation from code
tags: [documentation, api, openapi, swagger]
---

# API Documentation Process

Follow these steps to create complete API documentation:

## 1. Analyze the API

Identify all API endpoints and their details:
- HTTP methods (GET, POST, PUT, DELETE, PATCH)
- URL paths and parameters
- Request body schemas
- Response formats
- Authentication requirements
- Error responses

## 2. Load Documentation Standards

Review the documentation guidelines:
- Load `reference.md` for API documentation best practices
- Load `examples.md` to see well-documented API examples

## 3. Document Each Endpoint

For every API endpoint, include:

### Endpoint Overview
- **Method & Path**: `POST /api/users`
- **Description**: What the endpoint does
- **Authentication**: Required auth method
- **Rate Limiting**: Request limits if applicable

### Request Details
- **Headers**: Required and optional headers
- **Path Parameters**: URL parameters with types
- **Query Parameters**: Optional filters/options
- **Request Body**: JSON schema with examples

### Response Details
- **Success Response**: Status code and body schema
- **Error Responses**: All possible error codes
- **Examples**: Real request/response examples

## 4. Generate Documentation

Use the documentation generator:
```bash
python scripts/generate_docs.py <api_file> <format>
```

Supported formats:
- `openapi` - OpenAPI 3.0 specification
- `markdown` - Human-readable markdown
- `postman` - Postman collection

## 5. Add Usage Examples

Include practical examples:
- cURL commands
- JavaScript/Python code samples
- Common use cases
- Integration patterns

## 6. Document Authentication

Clearly explain:
- How to obtain credentials
- Where to include auth tokens
- Token expiration and refresh
- Permission levels
