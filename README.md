The <b> Movie Correlation project </b> aimed to generate a correlation matrix to determine highly correlated features in the movies.csv dataset. The features budget and gross earnings have a high correlation, whereas the company and budget have a low correlation value.
</br>
<p> First import pandas, seaborn, and matplotlib libraries. Then read in the data found on the Kaggle website 
(https://www.kaggle.com/datasets/danielgrijalvas/movies?resource=download) and display the first 5 rows of data.</p>
<img src="/images/Original_data-First5rows.png" width=1000>
<p> Dimesionality of the data frame - 7668 rows and 15 columns </p>
<img src="/images/Dimensionality_of_original_dataframe.png" width=100>
<p> Finding null values in each columns by looping through the data. </p>
<img src="/images/Counting_null_in_each_columns.png" width=300>
<p> After dropping all the rows with null values and duplicates, print the information about the dataframe. </p>
<img src="/images/Dataframe_info.png" width=300>
<p> Changing the datatypes from float to integer in two columns (Gross and Budget)  </p>
<img src="/images/Float_to_integertype_in_gross_and_budget.png" width=900>
<p> Extracting year from 'released' column and storing it in a new column 'year correct' and displying first 5 rows of data
after sorting 'Gross' data values in descending order.</p>
<img src="/images/New_column_yearcorrect_and_gross_descending.png" width=1000>
<p> Scatterplot shows positive relationship between budget and gross earnings variables. </p>
<img src="/images/Scatterplot-Budget_vs_Grossearnings.png" width=500>
<p> Plotting relationship between budget and gross earnings using regplot function.</p>
<img src="/images/Regplot-Budget_vs_Grossearnings.png" width=500>
<p> The Correlation matrix table for the columns with numeric values shows high correlation value(0.74) for budget and gross earnings</p>
<img src="/images/Correlation_Matrix_table.png" width=500>
<p> Heat map showing color encoded matrix for numerical features.</p>
<img src="/images/Heat_map-Numeric_features.png" width=500>
<p> Converting all the categorical feature values to numerical in order to display the heatmap of all features</p>
<img src="/images/Numerized_Dataframe.png" width=900>
<p> Heat map showing color encoded matrix for all features. </p>
<img src="/images/Heat_map-All_features.png" width=500>
<p> Generate the matrix pairs table as shown below </p>
<img src="/images/Matrix_Pairs.png" width=300>
<p> Sorting the matrix pairs with descending correlation values</p>
<img src="/images/Sorted_Matrix_Pairs.png" width=300>
<p> Displaying only the variable pairs that has the correlation value more than 0.5.</p>
<img src="/images/High_Correlated_Matrix_Pairs.png" width=300>



