Automated UI tests for http://uitestingplayground.com using Playwright (Python).

The project demonstrates two implementations:
- synchronous API (`sync_api`)
- asynchronous API (`async_api`)

## Tech Stack
- Python 3.11+
- Playwright
- pytest
- pytest-asyncio
- pytest-syncio
- urllib3

## Performance comparison

| Version     | Execution time |
|-------------|----------------|
| sync_api    | 7m 4s          |
| async_api   | 8s 98ms        |

## Covered scenarios
- Dynamic ID handling
- Class attribute changes on hover
- Handling hidden elements
- Explicit waits for dynamically loaded content
- AJAX-based data loading
- Client-side delay handling
- Text input interactions
- Scroll into view behavior
- Overlapped elements interaction
- Shadow DOM handling
- Text normalization (non-breaking spaces)
- Synchronization with AJAX responses

## Project Structure
config/        # config files
pages/         # Page Object Model
tests/         # test cases
test_files/    # upload/download test data
conftest.py    # pytest fixtures
pytest.ini     # markers & logging config

## Run tests
# all tests
poetry run pytest

# tests for a specific page
poetry run pytest -m <marker>
Full list of markers is defined in pytest.ini.

## Purpose
This project demonstrates:
- UI automation skills
- Playwright async vs sync comparison
- handling dynamic web elements

## Why this project
This project demonstrates practical QA automation skills including:
- working with dynamic and unstable UI elements
- handling async operations in Playwright
- comparison of sync vs async execution models
- scalable test structure using Page Object Model