# Tech Supply Chain Tracker & Geo-Impact Analytics Pipeline
A data engineering pipeline that scrapes technology supply chain headlines, uses LLMs to strcuture and analyse risk profiles, and visualises geopolitical impact centres on an interactive web dashboard.

---

## Key Freatures
1. Automated Web Scraping from technical sources.
2. Processing unstructured news narratives into structured JSON file using Llama 3.3 model.
3. Implemented standard decoupled environment configurations to protect operational infrastrcuture secrets.
4. Constructing a responsive data dashboard to visualise data.

---

## Tech Stack
1. Language: Python
2. Data Sources: Beautiful Soup 4/ Requests
3. Inference Engine: Llama -3.3-70b-versatile (Groq Cloud Client API)
4. Environment Management: Python-Dotenv/OS System Management
5. Data Manipulation: Pandas/ JSON Core Libraries
6. Visulisation Layer: Streamlit/Folium Web Maps/Streamlit-Folium

---

## Project Root
1. Webscraping_Digitimes.ipynb #Web scraping HTML news feeds to local storage
2. webscraping_digitimes_supply_chain.json #Raw web scraping data 
3. Extraction_Standardization_Digitimes.ipynb #Transforming raw data into structured JSON data
4. standardised_entities.json #Standardised data
5. app.py #Streamlit UI layout


