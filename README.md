# TIH Assignment - Sales Data Exploratory Data Analysis

A comprehensive data analysis and scripting project focused on processing, cleaning, and extracting insights from large-scale sales datasets. This repository contains structured Python utilities alongside an advanced exploratory data analysis (EDA) pipeline implemented via Jupyter Notebooks.

---

## 📂 Repository Structure

The project is organized as follows:

```text
├── 14-Exploratory_data_analysis_with_sales_data_Summer_2026.ipynb  # Main EDA & Data Visualization Notebook
├── q1_tih_assn.py to q8_tih_assn.py                              # Problem-specific modular Python scripts
├── sales.csv                                                     # Source dataset (~150k+ records)
└── README.md                                                     # Project documentation

```

* **`14-Exploratory_data_analysis_with_sales_data_Summer_2026.ipynb`**: The primary analytical core of the assignment, featuring statistical summaries, data distribution plots, and trend investigations on the 2026 sales lifecycle.
* **`q1_tih_assn.py` through `q8_tih_assn.py**`: Clean, standalone scripts addressing individual logical or algorithmic requirements outlined in the assignment criteria.

---

## 🛠️ Tech Stack & Dependencies

This project relies on core Python data science libraries. To set up your local environment, ensure you have Python installed, then run:

```bash
pip install pandas numpy matplotlib seaborn notebook

```

* **Data Manipulation:** `pandas`, `numpy`
* **Data Visualization:** `matplotlib`, `seaborn`
* **Environment:** Jupyter Notebook / IPython Kernel

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone [https://github.com/Alpha-Beta-810/TIH_Assignment.git](https://github.com/Alpha-Beta-810/TIH_Assignment.git)
cd TIH_Assignment

```

### 2. Running the Python Scripts

You can execute any of the standalone task scripts directly from your terminal:

```bash
python q1_tih_assn.py

```

### 3. Launching the EDA Notebook

To inspect the interactive visualizations and markdown summaries, boot up the Jupyter interface:

```bash
jupyter notebook

```

Click open `14-Exploratory_data_analysis_with_sales_data_Summer_2026.ipynb` and run the cells sequentially.

---

## ⚙️ Development Practices

* **Clean Caching:** A `.gitignore` file is used to suppress system artifacts (`__pycache__/`, `.ipynb_checkpoints/`) keeping the version history minimal and efficient.
* **Data Privacy / Optimization:** Large runtime files or structural deviations are intentionally isolated to safeguard rapid repository fetching.

```
---

