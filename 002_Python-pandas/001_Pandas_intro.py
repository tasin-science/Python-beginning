#### pandas

import pandas as pd

### creating a simple series
data = pd.Series([1,2,3,4,5])
print(data)

print("\n\n\n")

### Creating a dataframe from dictionary
source = {
    'Name' : ['Tasin', 'Rafiq', 'Alam'],
    'Age' : [22,22,23],
    'Score' : ['A+', 'A', 'A-']
}
df = pd.DataFrame(source)
print(df)
print(type(df))

print("\n\n\n")


### Reading a Spreadsheet file
df = pd.read_csv("Datasheet/Dataset_Lab_Test.csv")
print(df, "\n\n\n")




### Show Rows and Columns
rows, columns = df.shape
print("Rows are: ", rows, "\nColumns are: ", columns)

print("\n\n\n")


### head() and tail() method
print(df.head(), "\n\n\n") ## head() method
print(df.head(10), "\n\n\n") ## first 10 rows
print(df.tail(), "\n\n\n") ## tail() method
print(df.tail(10), "\n\n\n") ## last 10 rows


### creating new column
df['New_Col'] = 0
print(df, "\n\n\n")
#<>
## creating new column with arithmetic expression
df['A+B+C'] = df['Product_A'] + df['Product_B'] + df['Product_C']
print(df, "\n\n\n")
#<>
## creating new column with a set of numbers
df['Index'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
print(df, "\n\n\n")

