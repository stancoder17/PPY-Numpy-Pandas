# PPY-Numpy-Pandas
A task to practice Python's Numpy and Pandas libraries

## 1. Generate Random Data
Generate 10,000 integers in the range from -3 to 20 and store them in a list.

## 2. Compute Statistics
Calculate and display the following statistics:
- Mean  
- Median  
- Maximum value  
- Minimum value  
- Percentage of numbers that are smaller than three standard deviations from the mean  

## 3. Create a DataFrame
Create a `DataFrame` with two columns:
- `number` — containing all unique numbers from the generated list  
- `is_negative` — `True` if the number is negative, otherwise `False`  

## 4. Filter the DataFrame
Remove all rows from the `DataFrame` where the number is negative.

## 5. Generate a Histogram
Create a histogram showing the frequency of occurrence of each number:
- X-axis: numbers  
- Y-axis: frequency of occurrence
  
## 6. Save Results to CSV
Save the filtered data (after step 4) to a new CSV file named "Data_{mean}_{std}.csv", where:
- `mean` is the mean value  
- `std` is the standard deviation
  
Both values should be calculated from the data after step 4.
