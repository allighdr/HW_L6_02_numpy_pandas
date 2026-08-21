# 📊 Traffic Violations Data Analysis - Pandas & Matplotlib
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-Data%20Visualization-orange?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Status">
</p>
---
## 🇮🇷 توضیحات پروژه (Persian / Farsi)
در این پروژه به تحلیل داده‌های مربوط به تخلفات رانندگی با استفاده از کتابخانه‌های قدرتمند پانداس و مت‌پلات‌لیب پرداخته شده است. 
با توجه به عدم دسترسی به فایل اصلی `traffic_violations.csv` در زمان انجام پروژه، از یک اسکریپت پایتون به نام `script_of_creating_traffic_violation.py` جهت تولید داده‌های شبیه‌سازی‌شده (Mock Data) استفاده گردید[span_0](start_span)[span_0](end_span). 
این اسکریپت یک مجموعه داده‌ی جامع شامل **یک میلیون رکورد** تخلف رانندگی تولید می‌کند که دارای تنوع بالایی است[span_1](start_span)[span_1](end_span). داده‌های تولید شده در فایل CSV خروجی شامل موارد زیر می‌باشند[span_2](start_span)[span_2](end_span):
* تاریخ و زمان رخداد تخلف در بازه سال‌های مختلف
* پلاک‌های متنوع خودروها (شامل حروف بزرگ و کوچک جهت بررسی فرآیند پاک‌سازی داده‌ها)
* نام شهرهای مختلف و نوع وسیله نقلیه (خودرو، کامیون، موتور سیکلت و ...)
* نوع تخلف، سرعت مجاز، سرعت ثبت‌شده توسط دوربین، مبلغ جریمه و وضعیت پرداخت آن.
---
## 🇬🇧 🚀 About the Project (English)
This repository contains a comprehensive collection of practical exercises focused on **Data Manipulation, Time-Series Analysis, and Data Visualization** using **Pandas** and **Matplotlib**. The project focuses on cleaning, aggregating, and visualizing a large dataset of traffic violations.
> **📌 Important Note Regarding Visualizations:**  
> Exercises 5, 6, and 7 were initially created as separate scripts (`Exercise_5.py`, `Exercise_6.py`, and `Exercise_7.py`) to generate individual plots (Line Chart, Histogram, and Scatter Plot). In order to meet the project's requirement of displaying all three subplots within a single figure, an additional combined script named `Final_Figure_Exercise.py` has been provided. This script integrates the outputs of these three exercises into one cohesive dashboard.
## 📂 Project Structure

| File Name | Description | Key Topics Covered |
| :--- | :--- | :--- |
| **`script_of_creating_traffic_violation.py`** | Mock Data Generator | Random sampling, Datetime generation, Categorical data creation[span_3](start_span)[span_3](end_span) |
| **`traffic_violations.csv`** | The Dataset | 1,000,000 records of generated traffic violations[span_4](start_span)[span_4](end_span) |
| **`Exercise_1.py`** | Data Cleaning & Preparation | Datetime conversion (`to_datetime`), Date components (`dt`), String manipulation (`upper`)[span_5](start_span)[span_5](end_span) |
| **`Exercise_2.py`** | Data Aggregation | Grouping (`groupby`), Named Aggregation (`agg`), Boolean calculations |
| **`Exercise_3.py`** | Pivot Tables | Cross-tabulation (`pivot_table`), Data normalization, Index mapping (`idxmax`) |
| **`Exercise_4.py`** | Time Series Analysis | Datetime indexing (`set_index`), Time resampling (`resample`) |
| **`Exercise_5.py`** | Line Chart Visualization | Subplots creation, Line plotting, Grid configuration, Plot Annotations |
| **`Exercise_6.py`** | Histogram Visualization | Distribution plotting (`hist`), Binning, Customizing edges and colors |
| **`Exercise_7.py`** | Scatter Plot Visualization | Bubble charts (`scatter`), Dynamic marker sizes, Iterative point annotation |
| **`Final_Figure_Exercise_5_6_7.py`** | Final Dashboard | Combining multiple subplots (`nrows=3`), Adjusting layout (`tight_layout`) |
| **`*.png` files** | Plot Outputs | Rendered charts and the final combined figure |

---
> **Author:** Ali Ghaderi  
> **Course:** Data Engineering & Scientific Computing (Pandas & Matplotlib)