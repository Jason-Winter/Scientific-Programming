# Scientific Programming

## Project: Relationship Between Vaccination Rates, Case Numbers, and Deaths from COVID-19 in Switzerland

### Group Members
- David Schofield  
- Jason Winter  
- Aaron Näf  

### Objective  
To investigate how COVID-19 vaccination rates relate not only to reported case numbers but also to deaths in Switzerland. The analysis is based on weekly aggregated data, exploring whether vaccination rollouts influenced infection and mortality rates.

### Data Sources  
- [Bundesamt für Gesundheit (BAG)](https://www.covid19.admin.ch/) — primary source for COVID-19 cases, deaths, and vaccination data in Switzerland  
- [Our World in Data (OWID)](https://github.com/owid/covid-19-data) — used for reference population figures and background data  

### How to Run the Project  
1. Open the notebook: `notebooks/02_data_preparation_analysis.ipynb`  
2. Required Python packages: `pandas`, `matplotlib`, `scipy`, `sqlite3`  

### Project Highlights  
- 💾 **Data storage**: All data is imported from a local **SQLite** database  
- 🧹 **Data preparation**: Includes parsing dates, aggregating weekly data, and filling missing values  
- 📊 **Visualizations**: Time series and boxplots of cases, vaccinations, and deaths  
- 📈 **Statistical analysis**: A t-test compares weekly deaths before and after vaccine introduction, including the p-value  
- 🔄 **GitHub** used for version control; full code and data workflows are documented in a Jupyter Notebook  
