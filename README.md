# Redis Rate Limiter

A FastAPI project implementing dynamic rate limiting using Redis.

## Features

- Group-based rate limiting (Gold, Silver, Bronze, Default)
- Customizable request limits
- Stores client IP request counts in Redis
- Resets limit every 60 seconds
- Middleware integration for FastAPI

## Tech Stack

- Python 3.11
- FastAPI
- Redis


## Setup

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
