# Intro-to-python-assignments

## Week1
### Instructions:

#### Basic Calculator Program
- Create a simple Python program that asks the user  to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
- Perform the operation based on the user's input and print the result.
- Example: If a user inputs `10`, `5`, and `+`, your program should display `10 + 5 = 15`.

#### Objective
Practice creating Python programs to perform arithmetic and string, experimenting with variables and exploring data types.

## Week2
### Instructions:

1. Create an empty list called **my_list**.
2. Append the following elements to **my_list: 10, 20, 30, 40**.
3. Insert the value **15** at the second position in the list.
4. Extend **my_list** with another list: **[50, 60, 70]**.
5. Remove the last element from **my_list**.
6. Sort **my_list** in ascending order.
7. Find and print the index of the value **30** in **my_list**.

## Week3
### Instructions:

1. Create a function named **calculate_discount(price, discount_percent)** that calculates the final price after applying a discount. The function should take the original price **(price)** and the discount percentage **(discount_percent)** as parameters. If the discount is **20%** or higher, apply the discount; otherwise, return the original price.
2. Using the **calculate_discount** function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price

## Week4: File Handling and Exception Handling

### Instructions

- **File Read & Write Challenge**: Create a program that reads a file and writes a modifies version to a new file.
- **Error Handling Lab**: As the user for a filename and handle errors if it doesn't exist or can't be read.

**Outcomes**
- Managing files efficiently in Python
- Ensuring error-free code that gracefully handles unexpected issues.
- Build strong, robust applications

## Week5: Object Oriented Programming

### Instructions

**Activity 1: Design Your Own Class!**

1. Create a **class** representing anything you like (a `Smartphone`, `Book`, or even a `Superhero!`).
2. Add **attributes** and **methods** to bring the class to life!
3. Use **constructors** to initialize each object with unique values.
4. Add an inheritance layer to explore polymorphism or encapsulation.

**Activity 2: Polymorphism Challenge**
Create a program that includes animals or vehicles with the same action (like `move()`). However, make each class define `move()` differently (for example, `Car.move()`prints "Driving", while `Plane.move()`prints "Flying").

## Week7: Analyzing Data with Pandas and Visualizing Results with Matplotlib

### Objectives for the assignment
- To load and analyze a dataset using the pandas library in Python.
- To create simple plots and charts with the matplotlib library for visualizing the data.

### Submission Requirements
- Suubmit a Jupyter notebook (.ipynb file) or Python script (.py file) containing:
1. Data loading and exploration steps.
2. Basic data analysis results.
3. Visualizations.
4. Any findings or observations.

### Task 1: Load and Explore the Dataset
1. Choose a dataset in CSV format (for example, you can use datasets like the Iris dataset, a sales dataset, or any dataset of your choice).
2. Load the dataset using pandas.
3. Display the first few rows of the dataset using `.head()` to inspect the data.
4. Explore the structure of the dataset by checking the data types and any missing values.
5. Clean the dataset by either filling or dropping any missing values.

### Task 2: Basic Data Analysis
1. Compute the basic statistics of the numeral columns (e.g.,mean, median, standard deviation) using `.describe()`.
2. Perform groupings on a categorical column (for example, species, region, or department) and compute the mean of a numerical column for each group.
3. Identify any patterns or interesting findings from your analysis

### Task 3: Data Visualization
1. Create at least four different types of visualizations:
    - **Line chart** showing trends over time (for example, a time series of sales data).
    - **Bar chart** showing the comparison of a numerical  value accross categories (e.g., average petal length per species).
    - **Histogram** of a numerical  column to understand its distribution.
    - **Scatter plot** to visualize the relationship between two numerical columns (e.g., sepal length vs. petal lenght).

2. Customize your plots with titles, labels for axes, and legends where necessary.

### Additional Instructions
1. **Dataset Suggestions:**
    - You can use publicly available datasets from sites like Kaggle or UCI Machine Learning Repository.
    - The Iris dataset (a classic dataset for classification problems) can be accessed via sklearn.datasets.load_iris(), which can be used for the analysis.
2. **Plot Customization:**
    - Customize the plots using the `matplotlib` library to add titles, axis labels, and legends.
    - Use `seaborn` for additional plotting styles, which can make your charts more visually appealing.

3. **Error Handling:**
    - Handle possible errors during the file reading (e.g., file not found), missing data, or incorrect data types by using exception-handling mechanisms (`try`, `except`).
4. **Submission:**
    - Ensure your submission is complete with all necessary code and explanations. Make sure that each plot is properly labeled and provides insights into the dataset.

## 📊 Dataset Used

- Name: `iris_dataset.csv`
- Source: [Kaggle Datasets](https://www.kaggle.com/datasets)
- Columns:
  - `sepal length (cm)`
  - `sepal width (cm)`
  - `petal length (cm)`
  - `petal width (cm)`
  - `species`