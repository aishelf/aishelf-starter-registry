#!/usr/bin/env python3
"""
API documentation generator
Generates API docs in various formats
"""

import sys
import json
from pathlib import Path

def generate_markdown_docs(api_name):
    """Generate markdown API documentation"""
    
    doc = f"""# {api_name} API Documentation

## Overview

Brief description of the {api_name} API.

**Base URL:** `https://api.example.com/v1`  
**Authentication:** Bearer Token  
**Rate Limit:** 1000 requests/hour

---

## Authentication

All requests require authentication using a Bearer token:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## Endpoints

### List Items
`GET /items`

Retrieves a paginated list of items.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| page | integer | No | 1 | Page number |
| limit | integer | No | 20 | Items per page |

**Response (200 OK):**
```json
{{
  "data": [
    {{
      "id": "string",
      "name": "string",
      "createdAt": "datetime"
    }}
  ],
  "pagination": {{
    "page": 1,
    "limit": 20,
    "total": 100
  }}
}}
```

**Example:**
```bash
curl -X GET "https://api.example.com/v1/items?page=1&limit=20" \\
  -H "Authorization: Bearer YOUR_TOKEN"
```

---

### Create Item
`POST /items`

Creates a new item.

**Request Body:**
```json
{{
  "name": "string (required)",
  "description": "string (optional)"
}}
```

**Response (201 Created):**
```json
{{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "createdAt": "datetime"
}}
```

**Error (400 Bad Request):**
```json
{{
  "error": "Validation failed",
  "details": [
    {{
      "field": "name",
      "message": "Name is required"
    }}
  ]
}}
```

**Example:**
```bash
curl -X POST "https://api.example.com/v1/items" \\
  -H "Content-Type: application/json" \\
  -H "Authorization: Bearer YOUR_TOKEN" \\
  -d '{{
    "name": "New Item",
    "description": "Item description"
  }}'
```

---

## Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input |
| 401 | Unauthorized - Missing or invalid token |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error |

---

## Rate Limiting

Rate limits are enforced per API key:
- **Limit:** 1000 requests per hour
- **Headers:** `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Changelog

### v1.0.0 (2024-01-15)
- Initial release
- Basic CRUD operations
- Authentication support
"""
    
    return doc

def generate_openapi_spec(api_name):
    """Generate OpenAPI 3.0 specification"""
    
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": f"{api_name} API",
            "version": "1.0.0",
            "description": f"API documentation for {api_name}"
        },
        "servers": [
            {
                "url": "https://api.example.com/v1",
                "description": "Production server"
            }
        ],
        "paths": {
            "/items": {
                "get": {
                    "summary": "List items",
                    "parameters": [
                        {
                            "name": "page",
                            "in": "query",
                            "schema": {"type": "integer", "default": 1}
                        },
                        {
                            "name": "limit",
                            "in": "query",
                            "schema": {"type": "integer", "default": 20}
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Successful response",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "data": {"type": "array"},
                                            "pagination": {"type": "object"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    return json.dumps(spec, indent=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_docs.py <api_name> [format]")
        print("Formats: markdown (default), openapi")
        sys.exit(1)
    
    api_name = sys.argv[1]
    format_type = sys.argv[2] if len(sys.argv) > 2 else 'markdown'
    
    print(f"\n{'='*60}")
    print(f"Generating {format_type.upper()} documentation for {api_name}")
    print(f"{'='*60}\n")
    
    if format_type == 'markdown':
        print(generate_markdown_docs(api_name))
    elif format_type == 'openapi':
        print(generate_openapi_spec(api_name))
    else:
        print(f"Unsupported format: {format_type}")
        sys.exit(1)
    
    print(f"\n{'='*60}\n")
