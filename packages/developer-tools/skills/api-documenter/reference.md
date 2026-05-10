# API Documentation Reference

## Documentation Structure

### 1. Overview Section
```markdown
# API Name

Brief description of what the API does.

**Base URL:** `https://api.example.com/v1`  
**Authentication:** Bearer Token  
**Rate Limit:** 1000 requests/hour
```

### 2. Authentication
```markdown
## Authentication

All requests require a Bearer token in the Authorization header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

To obtain a token, use the `/auth/login` endpoint.
```

### 3. Endpoints

For each endpoint, document:

#### HTTP Method & Path
```markdown
### Create User
`POST /users`
```

#### Description
```markdown
Creates a new user account with the provided information.
```

#### Request Headers
```markdown
| Header | Required | Description |
|--------|----------|-------------|
| Content-Type | Yes | Must be `application/json` |
| Authorization | Yes | Bearer token |
```

#### Request Body
```markdown
```json
{
  "name": "string (required)",
  "email": "string (required, valid email)",
  "role": "string (optional, default: 'user')"
}
```
```

#### Response
```markdown
**Success (201 Created)**
```json
{
  "id": "uuid",
  "name": "string",
  "email": "string",
  "role": "string",
  "createdAt": "ISO 8601 datetime"
}
```

**Error (400 Bad Request)**
```json
{
  "error": "Validation failed",
  "details": [
    {
      "field": "email",
      "message": "Invalid email format"
    }
  ]
}
```
```

#### Example
```markdown
**Request:**
```bash
curl -X POST https://api.example.com/v1/users \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin"
  }'
```

**Response:**
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john@example.com",
  "role": "admin",
  "createdAt": "2024-01-15T10:30:00Z"
}
```
```

## HTTP Status Codes

Document all possible status codes:

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful GET, PUT, PATCH, DELETE |
| 201 | Created | Successful POST that creates a resource |
| 204 | No Content | Successful request with no response body |
| 400 | Bad Request | Invalid request data |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Authenticated but not authorized |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Resource already exists |
| 422 | Unprocessable Entity | Validation failed |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Internal Server Error | Server error |
| 503 | Service Unavailable | Temporary unavailability |

## Error Response Format

Standardize error responses:

```json
{
  "error": "Brief error message",
  "code": "ERROR_CODE",
  "details": [
    {
      "field": "fieldName",
      "message": "Specific error for this field"
    }
  ],
  "requestId": "uuid",
  "timestamp": "ISO 8601 datetime"
}
```

## Pagination

Document pagination pattern:

```markdown
### Pagination

List endpoints support pagination using query parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| page | integer | 1 | Page number (1-indexed) |
| limit | integer | 20 | Items per page (max: 100) |
| sort | string | createdAt | Field to sort by |
| order | string | desc | Sort order (asc/desc) |

**Response includes pagination metadata:**
```json
{
  "data": [...],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150,
    "totalPages": 8,
    "hasNext": true,
    "hasPrev": false
  }
}
```
```

## Versioning

Document API versioning strategy:

```markdown
## Versioning

The API uses URL versioning: `/v1/`, `/v2/`, etc.

- **Current Version:** v1
- **Deprecated Versions:** None
- **Breaking Changes:** Announced 6 months in advance
```

## Rate Limiting

```markdown
## Rate Limiting

Rate limits are enforced per API key:

- **Standard:** 1000 requests/hour
- **Premium:** 10000 requests/hour

Rate limit headers in responses:
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640000000
```

When exceeded, returns 429 with retry-after header.
```

## Best Practices Checklist

- [ ] Every endpoint is documented
- [ ] All parameters are described with types
- [ ] Request/response examples are provided
- [ ] Error responses are documented
- [ ] Authentication is clearly explained
- [ ] Rate limits are specified
- [ ] Versioning strategy is documented
- [ ] Pagination is explained (if applicable)
- [ ] Code examples in multiple languages
- [ ] Changelog for API changes
