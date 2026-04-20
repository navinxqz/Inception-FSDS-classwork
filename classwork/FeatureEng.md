# Feature Engineering
Feature Engineering is the process of creating new features from existing data to improve the performance of machine learning models. It involves transforming raw data into a format that is more suitable for modeling, often by extracting relevant information or creating new variables that capture important patterns in the data.

* From EDA we try to understand the meaning of the data and the relationship between different features. This understanding can help us identify which `features` are most important for our model and how we can create new features that capture important information.

* In Feature Engineering, we fix those problems that we identified in EDA. For example, if we have missing values in our data, we can create new features that indicate whether a value is missing or not. If we have categorical variables, we can create new features by encoding them into numerical values.

`GIGO` stands for "`Garbage In, Garbage Out`". It means that if we input poor quality data into our machine learning model, we will get poor quality results. Feature Engineering is important because it helps us to improve the quality of our data and create features that are more relevant to our model, which can lead to better performance.

That is why model training is not a big deal, feature engineering is the key to building a successful machine learning model. By creating new features that capture important information in our data, we can improve the performance of our model and make better predictions.

#### Data Load => EDA => Feature Engineering => Model Training => Model Evaluation

## In Feature Engineering:
1. Feature Transformation
    - Missing Value Handling
    - Handling Categorical Features
    - Outlier Detection
    - Feature Scaling (Easiest task)
2. Feature Construction
3. Feature Selection
4. Feature Extraction

### For Missing Value Handling:
1. Mean calculation
2. Median calculation (Apply when Outlier Present)
3. Mode calculation

### Handling Categorical Data:
1. One-Hot Encoding (1 for present and 0 for not present)

### Outlier Detection:
1. Linear Regression (Best fit line)

### Feature Scaling:
 1. Distance Calculation alg (K-nearest neighbor, SVM, etc)
 2. Standardization (scaling the data to have a mean of 0 and a standard deviation of 1)
 * Last step in feature engineering is to apply the model and evaluate the performance of the model. We can use different evaluation metrics such as accuracy, precision, recall, F1-score, etc to evaluate the performance of our model.