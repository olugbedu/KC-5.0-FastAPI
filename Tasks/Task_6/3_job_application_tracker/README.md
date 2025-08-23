# Job Application Tracker API (Task 3)

## Features
- Secure login (Basic Auth)
- Each user can only view **their own applications**
- Store applications in `applications.json`

## Endpoints
- `POST /applications/` → Add a new job application
- `GET /applications/` → View your own applications

## Example Users
```json
{
  "alice": {"password": "alicepass"},
  "bob": {"password": "bobpass"}
}
