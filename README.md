# GitHub Issue to Jira Automation

## Project Overview

This project automates Jira ticket creation from GitHub issues using GitHub Webhooks, Python Flask, and Jira REST APIs.

When a developer validates an issue in GitHub and comments `/jira` on the issue, a GitHub Webhook sends the payload to a Flask application hosted on an AWS EC2 instance. The Flask application processes the payload and automatically creates a Jira ticket using the GitHub issue title and description.

This automation eliminates manual Jira ticket creation and improves issue tracking efficiency.

---

## Problem Statement

In many software development teams:

1. QA Engineers or Developers raise issues in GitHub.
2. Developers validate the issue.
3. Developers manually create Jira tickets.
4. Repetitive ticket creation consumes time and effort.

This project automates the GitHub-to-Jira ticket creation workflow.

---

## Solution

When a developer comments `/jira` on a GitHub issue:

- GitHub Webhook is triggered.
- Flask application receives the payload.
- Application extracts issue details.
- Jira REST API is called automatically.
- Jira ticket is created.

---

## Architecture

```text
GitHub Issue Created
        │
        ▼
Developer comments "/jira"
        │
        ▼
GitHub Webhook
        │
        ▼
AWS EC2
Flask Application
(/createJira)
        │
        ▼
Process Payload
        │
        ├── Issue Title
        └── Issue Description
        │
        ▼
Jira REST API
        │
        ▼
Create Jira Ticket
        │
        ▼
Success Response
```

---

## Technology Stack

- Python
- Flask
- Requests Library
- GitHub Webhooks
- Jira REST API
- AWS EC2
- JSON
- Environment Variables

---

## Prerequisites

### AWS

- EC2 Instance
- Security Group allowing Port 5000

### Software

- Python 3
- pip

### Accounts

- GitHub Account
- Jira Account

### Python Libraries

- Flask
- Requests

---

## Environment Variables

```bash
export URL=<jira_api_url>
export EMAIL_ID=<jira_email>
export API_TOKEN=<jira_api_token>
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/github-issue-to-jira-automation.git

cd github-issue-to-jira-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python3 github-jira-automation.py
```

Output:

```text
* Running on http://0.0.0.0:5000
```

---

## GitHub Webhook Configuration

Navigate to:

```text
Settings
→ Webhooks
→ Add Webhook
```

Configure:

```text
Payload URL:
http://<EC2-Public-DNS>:5000/createJira

Content Type:
application/json
```

---

## Workflow

### Step 1

Create GitHub Issue

Example:

```text
Create functionality implementation needed
```

### Step 2

Developer validates issue.

### Step 3

Developer comments:

```text
/jira
```

### Step 4

GitHub Webhook sends payload.

### Step 5

Flask application receives payload.

### Step 6

Application extracts:

```python
issue_title
issue_description
```

### Step 7

Jira REST API creates ticket.

### Step 8

Jira work item is visible in Jira backlog.

---

## Screenshots

### GitHub Issue Created

`screenshots/issue_created.png`

### GitHub Comment

`screenshots/github_comment.png`

### EC2 Flask Application Running

`screenshots/ec2_flask_app_running.png`

### GitHub Webhook Configuration

`screenshots/webhook_url.png`

### Terminal Output

`screenshots/terminal_output.png`

### Jira Ticket Created

`screenshots/jira_ticket_created.png`

---

## Skills Demonstrated

- Python Automation
- REST APIs
- GitHub Webhooks
- Jira API Integration
- AWS EC2
- Flask
- JSON Processing
- Event-Driven Architecture
- Environment Variables
