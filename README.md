# 🚓 Racial Bias in U.S. Traffic Stops — Outcome-Based Predictive Modeling

## 📌 Overview

This project investigates **systemic racial bias in police traffic stops** using a novel **outcome-sensitive predictive modeling approach**. Rather than analysing stop frequency or hit rates, it tests whether **the outcome of a stop** (e.g., citation, arrest) can be predicted using **race-neutral features**, and how prediction accuracy changes when race is included.

> Conducted as one of two capstone research projects during the **Master of Data Analysis** at **Queensland University of Technology (QUT)**.

---

## 👤 Author

**Alex Conroy**  
Master of Data Analysis — QUT  
📚 Independent Research Dissertation  
📍 Project 1 of 2

---

## 🎯 Project Goal

> Can we model the **decision to arrest or cite a driver** without knowing their race — and does model accuracy improve if race is included?

This reframes the problem from stop bias to **decision-making sensitivity**, helping avoid confounders present in traditional hit rate or stop frequency analysis.

---

## 📊 Data Sources

- **Stanford Open Policing Project (SOP):** Aggregated traffic stop data across U.S. states
- **U.S. Census Bureau ZCTA Crosswalk:** Demographic context by ZIP code
- **Google Maps Geocoding API:** Reverse-geocoding of stop locations (ZIP → ZCTA)

---

## 🧠 Methodology

### 📍 Geospatial Enrichment (Python)
- Reverse geocoded ZIP codes to ZCTA using Google Maps API
- Merged with U.S. Census population and race/ethnicity data

### 📈 Statistical Modeling (R)
- Constructed multinomial logistic regression models using `nnet::multinom()`
- Compared outcome prediction accuracy with and without racial features
- Evaluated across states (e.g. Colorado, North Carolina) and time windows

---

## 💡 Key Results

| Metric                 | With Race | Without Race |
|------------------------|-----------|---------------|
| Predictive Accuracy    | ↑ Improved | ↓ Decreased   |
| State-Level Consistency| High       | High          |
| Interpretability       | Transparent| Transparent   |

✅ Racial identifiers **increase predictive power**, implying bias in outcome decisions  
✅ Shows **decision-level sensitivity** to race, not just stop frequency bias  
⚠️ Ethical limitation: models reflect *outcomes*, not necessarily officer intent

---

## 🔎 Project Structure
racial-bias-traffic-stops/ ├── data/ │ ├── sop_subset.csv # Subsampled SOP stop data │ └── census_zcta_mapping.csv # ZIP-to-ZCTA crosswalks │ ├── notebooks/ │ ├── zcta_cluster_analysis.ipynb # Geospatial and census merging (Python) │ ├── reverse_geo_code.ipynb # Google Maps geocoder (Python) │ ├── analysis/ │ └── SOPModel_all_test.Rmd # Multinomial regression modeling (R) │ ├── report/ │ ├── Report DRAFT.pdf # Draft dissertation write-up │ ├── IFN704_Project_Proposal.pdf # Initial research proposal │ └── IFN704_Alex_Conroy_Presentation.pdf # Final presentation slides │ ├── research.txt # Raw notes and research log ├── README.md


---

## 🧪 Tools & Libraries

- **Python:** pandas, requests, geopy, geocoding APIs  
- **R:** `nnet`, `car`, `dplyr`, `ggplot2`  
- **Jupyter + RMarkdown**: Mixed-language data science pipeline  
- **PDF Reporting:** Academic communication and presentation

---

## ⚠️ Limitations

- Models **cannot infer causality or intent**
- Data only includes **recorded stop outcomes**, not reasoning
- Geocoding errors or data gaps may introduce spatial noise
- SOP data completeness varies by state

---

## 🔮 Future Work

- Expand to additional states or newer SOP releases  
- Apply **causal inference** or counterfactual analysis  
- Integrate police bodycam metadata or context from court outcomes  
- Develop fairness-aware models using **sensitive feature auditing**

---

## 📄 License

This project uses public data from the **Stanford Open Policing Project** and the **U.S. Census Bureau**.  
No proprietary or confidential datasets were used.

---

## 🏆 Why This Matters

This project shows how **transparent, explainable modeling** and thoughtful geospatial analysis can support conversations around **bias, ethics, and decision fairness** — essential for data science in government, policy, and social impact sectors.






