#About the Project

This project provides a RESTful API service that offers detailed crime analysis data for Indian states, with a special focus on crimes against women. The API exposes multiple endpoints to retrieve state-wise statistics about various crime categories, gender-wise victim data, and yearly crime trends from authentic and processed datasets.

The aim is to empower developers, researchers, and policymakers by making crime data easily accessible and machine-readable, supporting data-driven decisions, research, and visualization in web or mobile apps.

##Features

State-wise Crime Data: Detailed crime statistics related to different categories of crimes against women.

Gender-wise Victim Data: Breakdowns of crime victims by gender and age.

Yearly Crime Trends: Historical crime data across years (2020, 2021, 2022) for each state.

Simple REST API: Easy-to-use API endpoints for quick integration.

JSON Response: Well-structured JSON output for all queries.

Case-insensitive Queries: State names can be queried regardless of letter case.

##How It Works

The API loads pre-processed CSV datasets on startup (df_women.csv, df1.csv, and df2.csv).

When a client sends a GET request to an endpoint with a state name, the API:

Filters the dataset(s) for that state.

Returns the relevant crime statistics or trend data.

Sends a JSON response with the requested information.

If the state is not found, an error message is returned.

##API Endpoints
Base URL
https://crime-analysis-inindia-api.onrender.com
Endpoints
Endpoint	Method	Description
/	GET	Health check — confirms API is running.
/women-crime/{state}	GET	Returns crime statistics against women for a state.
/gender-victims/{state}	GET	Returns gender-wise and age-wise victim data for a state.
/year-trend/{state}	GET	Returns yearly crime trend data (2020-2022) for a state.

Example API Usage
Get crime data against women in Bihar

GET https://crime-analysis-inindia-api.onrender.com/women-crime/Bihar
Response:

{
  "States": "Bihar",
  "Murder_with_Rape/Gang_Rape": 0,
  "Dowry_Deaths": 1057,
  "Abetment_to_Suicide_of_Women": 2,
  "Miscarriage": 0,
  "Acid_Attack": 3,
  "Cruelty_by_Husband_or_his_relatives": 1850,
  "Kidnapping_&_Abduction_of_Women_(Total)": 10190,
  "Procuration_of_Minor_Girls": 0,
  "women_Trafficking": 25,
  "Selling_of_Minor_Girls": 0,
  "Rape_cases": 881,
  "Assault_on_Women_with_Intent_to_Outrage_her_Modesty": 402,
  "Insult_to_the_Modesty_of_Women": 0,
  "Dowry_prohibition": 3580,
  "Procuring,_inducing_Children_for_the_sake_of_prostitution": 36,
  "Publishing_or_Transmitting_of_Sexually_Explicit_Material": 4,
  "Women_Centric_Cyber_Crimes_(Ex._Blackmailing/_Defamation/Morphing/_Fake_Profile)": 13,
  "Total_Crimes": 18043,
  "Total_Population": 12.7,
  "Women_sex_ratio": 891,
  "Estimated_Female_Pop": 5.983976731887889,
  "Crimes_Per_Lakh_Women": 30.1521894359
}
Installation and Running Locally
Clone the repo:

git clone <your-repo-url>
cd your-project-directory

Install dependencies:
pip install fastapi uvicorn pandas

Data/
├── df_women.csv
├── df1.csv
└── df2.csv
Run the API server locally:

uvicorn api.main:app --host 0.0.0.0 --port 8000
Test endpoints at http://localhost:8000

Contact
For any questions or collaboration, please reach out to:

Priya Kumari
Email: pandeypriya05052003@gmail.com
GitHub: (https://github.com/Priya-kumari-hub)
