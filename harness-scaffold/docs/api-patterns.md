# API Patterns

<!-- FILL IN: Your project's API design guidelines -->

## General Principles

- Use consistent naming conventions
- Validate input at system boundaries
- Return structured error responses
- Document public APIs

## Error Handling

- 4xx: Client errors (bad request, not found, unauthorized)
- 5xx: Server errors (unexpected failures)
- Always include a human-readable message in error responses
- Never expose stack traces or internal details in production

## Response Format

```json
{
  "data": {},
  "success": true,
  "message": "Operation successful"
}
```

## Versioning

<!-- FILL IN: URL-based, header-based, or other strategy -->
