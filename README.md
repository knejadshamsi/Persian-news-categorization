# Persian News Classifier

## Overview

This project, developed at Islamic Azad University, Tehran North Branch, introduces a Python-based Natural Language Processing (NLP) script that classifies news titles into four distinct categories. The script leverages machine learning techniques and NLP tools to process and categorize news data efficiently.

## Features

- **Data Preprocessing:** Custom function for tokenization, normalization, and cleaning of news titles.
- **Categorization:** Classifies news titles into four categories - Political, Sports, Economic, and Social.
- **Model Training and Testing:** Utilizes Naive Bayes classifier for training and testing the model.
- **Accuracy Assessment:** Includes functionality to assess the model's accuracy and generate performance reports.

## Technical Stack

- **Python Libraries:** pandas, seaborn, matplotlib, sklearn, TensorFlow
- **Machine Learning Techniques:** Naive Bayes Classification, TF-IDF Vectorization
- **Data Visualization:** Seaborn and Matplotlib for data plotting

## Installation

1. Clone the repository.
2. Install required Python libraries: `pandas`, `seaborn`, `matplotlib`, `sklearn`, `tensorflow`.
3. Place your dataset in a CSV format named "NLP datatset title.csv".

## Usage

1. Run the script to train the model using your dataset.
2. Input a news title when prompted.
3. The script will classify the news title into one of the four categories.

## Dataset

Your dataset should be a CSV file with at least two columns: 'Title' for the news title and 'category' for its corresponding category.

## Contributing

Contributions, issues, and feature requests are welcome.