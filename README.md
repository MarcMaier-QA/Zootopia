# Zootopia Animals Project

This project fetches animal information from the Animals API (API Ninja) and generates an HTML website displaying the results.

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
```
2. Create and activate your virtual environment (optional but recommended):
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. **API-KEY**
Create a .env file in the root directory with your API key:
API_KEY='your_api_key_here'


5. **Usage Text**

   Run the program:
   ```` python animals_web_generator.py````
Enter the name of an animal when prompted.
The program will generate animals.html with the results.
