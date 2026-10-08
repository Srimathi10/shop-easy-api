# shop-easy-api

Backend for the ShopEasy online store: customer accounts, login, cart, checkout and payments.

> ShopEasy is a fictional company used in the **Git in the Real World** course.

## Getting started

Requirements: Python 3.9+ and Git.

```bash
git clone <repository-url>
cd shop-easy-api
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Check that everything works before you change anything:

```bash
pytest              # run the test suite
python -m src.app   # run the local demo end to end
```

## Project layout

```
shop-easy-api/
├── src/
│   ├── app.py            command-line demo (python -m src.app)
│   ├── auth.py           password hashing and login
│   ├── checkout.py       cart, totals, checkout
│   ├── config.py         settings and feature flags
│   ├── email_service.py  outgoing email (kept in an outbox locally)
│   ├── logger.py
│   ├── payment.py        payment gateway client (fake locally)
│   └── user.py           customer accounts
├── tests/
└── .github/              CI workflow, CODEOWNERS, PR template
```

## How we work

- Every change starts with a Jira ticket (`SHOP-1234`).
- Never commit directly to `main`. It is protected.
- Create a branch from an up-to-date `main`: `feature/SHOP-1234-short-description`.
- Open a Pull Request using the template. CI must pass and a reviewer must approve.

See [CONTRIBUTING.md](CONTRIBUTING.md) for branch naming, commit messages and the review process.


## Development notes

Authentication and checkout logic are covered by automated tests. Run `pytest` before opening a pull request.

The command-line demo can be started with `python -m src.app`.
