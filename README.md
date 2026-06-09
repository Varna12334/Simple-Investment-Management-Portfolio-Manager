## Simple Investment Management — Portfolio Manager 📈
A lightweight tool designed to help you manage your investments (stocks and mutual funds), track your total invested value, and visualize your portfolio performance.

## Workflow
Code snippet
```mermaid
graph LR
    A[Add Investment] --> B[Store Record]
    B --> C[Calculate Totals]
    C --> D[Compute Profit/Loss]
    D --> E[Generate Summary & Charts]
    E --> F[Export Reports]
## Features
Track Investments: Easily record your stock and mutual fund holdings.

Performance Metrics: Automatically calculate total invested value and current profit/loss.

Visual Insights: Generate clear portfolio allocation charts and summary tables.

## Quick Start
### 1. Installation
Clone the repository and install the required dependencies:

#### Bash
git clone https://github.com/Varna12334/Simple-Investment-Management-Portfolio-Manager.git
cd Simple-Investment-Management-Portfolio-Manager
pip install -r requirements.txt
### 2. Usage
Run the main application to start managing your portfolio:

#### Bash
python portfolio.py
Project Structure
backend/: Core calculation logic.

#### data/: 
Contains sample_data.csv for initial testing.

#### frontend/:
UI components for the dashboard.

#### docs/: 
Supporting documentation and visual assets.
