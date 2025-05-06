Loan Defaulters' Demographic Visualizer
This project visualizes the demographics of individuals who have defaulted on loans, using big data tools and interactive dashboards. The aim is to uncover trends based on age, income, occupation, and gender to aid in risk assessment and financial decision-making.

## Project Overview
Objective: To analyze and visualize demographic patterns among loan defaulters.

## Technologies Used:

Amazon Web Services (AWS EMR & S3)

PySpark

Tableau

Dataset: Kaggle - Loan Defaulter Dataset

## System Architecture
Data is stored in AWS S3.

Processed using PySpark on AWS EMR.

Output visualized in Tableau Online using S3 connectors.

## Data Preprocessing Steps
Selected loan defaulters only (TARGET = 1)

Chose relevant columns: age, gender, income, occupation.

Converted birthdays to age

Removed nulls and outliers

Managed Data Missings

## Visualization Highlights
Age: Peak defaulters in the 30–34 age range

Income: Most defaulters in mid-income (€150K) group

Occupation: Majority from "Labourers"; few from IT or HR
