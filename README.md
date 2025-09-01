# Relational Database & Data Cleaning and Analysis Project

This project involved the creation of a clean, relational database from several disparate, provided data sets. The primary goal was to integrate all the information into a unified structure that is easy to query and analyze. 
A key challenge was to clean and validate the data before insertion, addressing issues such as missing information, null values, and inconsistent formatting.

The core identifiers used to link the data across all tables are State and County, which serve as the primary relationship keys. This ensures data integrity and allows for seamless joins between different data sets.

## Database Design

The core of this project is a robust relational database designed to support detailed data analysis. By normalizing and structuring the data, we can efficiently query and perform complex analyses that wouldn't be possible with the raw, unstructured data. 
The tables and their relationships, which are based on the cleaned State and County identifiers, were carefully designed after a thorough data cleaning process to ensure all information is accurate and connected correctly.

Here are the tables that make up the database:

### County Tax Rate

<img width="2508" height="1240" alt="countyTaxRate" src="https://github.com/user-attachments/assets/de92037a-e4b6-4928-a1fd-090fd6272b69" />

### Exports by State

<img width="2383" height="1206" alt="exportsByState_1" src="https://github.com/user-attachments/assets/6019a0a2-4db4-4340-ba21-e264247a7e17" />
<img width="2519" height="1251" alt="exportsByState_2" src="https://github.com/user-attachments/assets/17ec7278-8c3c-4196-a7f7-c3c1a6193824" />

### Median County Income

<img width="2507" height="1243" alt="medianCountyIncome" src="https://github.com/user-attachments/assets/f7ccdea0-02da-4411-b719-65b849939776" />

### State Tax Rate

<img width="2505" height="1237" alt="StateTaxRate" src="https://github.com/user-attachments/assets/9c696ac2-7c76-4671-bf52-87f0acae9383" />

### Unemployment By County

<img width="2514" height="1247" alt="UnemploymentByCounty" src="https://github.com/user-attachments/assets/fb13a413-8765-4d02-8694-6e7ad66abf58" />

### Usa County List

<img width="2507" height="1239" alt="UsaCountyList" src="https://github.com/user-attachments/assets/43455726-2ed5-44f5-a035-2e06ae9ed833" />

### Workforce Wages

<img width="2423" height="1206" alt="WorkforceWages_1" src="https://github.com/user-attachments/assets/af412f2e-8a1d-439f-be85-ff5900b52210" />
<img width="2517" height="1253" alt="WorkforceWages_2" src="https://github.com/user-attachments/assets/2df316fc-e9f3-448e-8836-dfc62ac87fcd" />

### Data Relation Visualization 

<img width="2251" height="1070" alt="DataVisualization" src="https://github.com/user-attachments/assets/23f933cd-1980-4efa-b5f2-2d2ec3f7f5d9" />

## SQL Queries

### Find all counties that have a state tax rate lower than 4% and an unemployment rate higher than 6%. Sort them by their Annual Total Wages (for all industries) from highest to lowest.

<img width="2250" height="1203" alt="2a" src="https://github.com/user-attachments/assets/f20a8b09-f800-4a62-9064-0cbb8e9633e1" />

### Find the 10 counties with the highest Annual Total Wages in the Service Providing industry that also have a Coefficient of Variation for Ton-Miles greater than 20 (for the year 2012) and a labor force over 7,500.

<img width="2250" height="1200" alt="2b" src="https://github.com/user-attachments/assets/e4719c4c-7d15-4ecc-b9d7-c144341325fa" />

### Find all counties with an Annual Average Pay under $40,000 and a local tax rate under 3%. Sort them from highest population to lowest.

<img width="2250" height="1202" alt="2c" src="https://github.com/user-attachments/assets/fa7c0455-498c-4f44-983b-b6011a2a38b3" />

### Find the 10 counties with the highest population whose 2012 exports value is over 25 trillion and also have a higher Annual Average Establishment Count in Construction than in Manufacturing.

<img width="2251" height="1201" alt="2d" src="https://github.com/user-attachments/assets/91859912-d3f6-4752-9227-513e111b6150" />

## Location Store:

### For every county in the United States and export a list of all counties sorted from highest score to lowest score. Generate an algorithm that gives a numerical score (ranging from 0 to 100) based on data and key factors that are specified by the customer.

## Customer Specifications:

### Location with relatively low average wages in the service-providing industry; Location with low tax rates; Location with high median income; Location with high unemployment

<img width="2497" height="1272" alt="ShipsAndCo_Code_2" src="https://github.com/user-attachments/assets/4fb632ae-6d14-4c4f-a361-0e1cfc1676c3" />
<img width="2510" height="1338" alt="ShipsAndCo_Code_1" src="https://github.com/user-attachments/assets/43c075b8-8c8f-49e2-a9e2-403bb492872d" />





