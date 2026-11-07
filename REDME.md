# Python Mini Projects Portfolio

This repository contains the Python mini projects I built while learning Python Foundations (Phase 0.5 of my DevOps + MLOps roadmap).

---

## Projects List

| No. | Project | Description | Status |
|-----|---------|-------------|--------|
| 1 | Weather CLI | Get real-time weather using OpenWeatherMap API | Completed |
| 2 | System Info Reporter | Display system information (CPU, RAM, Disk, OS) | Completed |
| 3 | File Organiser | Automatically organize files by extension | Completed |
| 4 | Password Generator | Generate strong passwords from command line | Upcoming |
| 5 | Log Parser | Read log files and generate reports | Upcoming |

---

## Project Details

### 1. Weather CLI
A command-line tool that fetches current weather data for any city.

**Features:**
- Uses OpenWeatherMap API
- API key stored securely in `.env`
- Supports command-line arguments (`argparse`)

**How to run:**
```bash
python weather.py --city Colombo