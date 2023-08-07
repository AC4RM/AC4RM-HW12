### Introduction
- This is the week 12 homework repository of ERMC K5455 (Applied Coding for Risk Mgmt) at Columbia University. 
- Please refer to Canvas for the homework deadline.

<hr>

### How to submit the homework

1. Similar to the previous homework, we would like to recreate the `time_it` decorator as a context manager.
   - Implement a context manager called `time_it` that will **print out** the execution time of the function nested in the `with` statement.
   - The context manager should print out a string following this format below:
     - `"The function takes <0.00125> seconds"`
   - You may use the functions from the Python [datetime](https://docs.python.org/3/library/datetime.html#timedelta-objects) module to calculate the time used.
2. Write SQL queries to do the following:
   - From the `customers` table, replace the missing values in `phone` column with `Unknown`. Order the result by `first_name` in ascending order and return the `customer_id` and `phone` columns in the result.
   - From the `orders` tale, create a new column called `category` based on the conditions below. Order the result by `order_date` in ascending order and return the `order_date` and `category` columns in the result.
     - For `order_date` in year `2019`, assign `Active`
     - For `order_date` in year `2018`, assign `Last Year`
     - For `order_date` in year `2017`, assign `Archived`
3. A classic use case of naive bayes is spam email classifier. The frequency of each unqiue token(word) is being used as the input features of the model.
   - Since the input features are frequency, we need to use a slightly different version of Naive Bayes called **Multinomial Naive Bayes**. You can find more details on the documentation page [here](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html).
   - Using the dataset below, train a multinomial naive bayes model to predict whether the email is spam or not spam. Return the model at the end of the function.
   - You may notice that the values in each column are actually float numbers. The reason is that this dataset use some pre-processing techniques called **TF-IDF**, which is one step beyond just counting the frequency. You can read more about from [here](https://en.wikipedia.org/wiki/Tf%E2%80%93idf).
4. Write a regular expression that matches all instances of the word "error" that are not preceded by the word "no". For example:
   - `text = "There is no error in this code. However, an unexpected error occurred during execution."`
   - `re.findall(regex_pattern, text) => ["error"]`
