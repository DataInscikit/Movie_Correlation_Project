
#importing libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.rcParams["figure.figsize"] = (18, 10)

# Reading data and displaying all rows and columns
df = pd.read_csv(r"/Users/lakshmi/Downloads/movies.csv")
pd.options.display.width= None
pd.options.display.max_columns= None
pd.set_option('display.max_rows', 7668)
pd.set_option('display.max_columns', 17)
print(df)

# looking for missing values
for col in df.columns:
    print(df[col].isnull().value_counts(), "\n")

#drop na rows and dupliate rows
df = df.dropna()
df = df.drop_duplicates()

#getting data info
df.info()

#changing Data types of columns
df['budget'] = df['budget'].astype(int)
df['gross'] = df['gross'].astype(int)
print(df.head(10))

#creating new column with release year
df['yearcorrect'] = df['released'].astype(str).str.split().str[2]
print(df.head(10))
print('\n')
df1 = df.sort_values(by=['gross'], inplace=False, ascending=False)
print(df1.head(10))

#scatterplot with budget vs gross earnings
plt.scatter(x=df['budget'], y=df['gross'])
plt.title('Budget vs Gross earnings')
plt.xlabel('Budget')
plt.ylabel('Gross earnings')
plt.show()

#plot budget vs gross earnings using seaborn
sns.regplot(x='budget',y='gross',data =df, scatter_kws={"color":"red"}, line_kws={"color":"blue"})
plt.show()

#generating correlation matrix
print(df.head(5))
Matrix = df.corr(method="pearson", numeric_only=True)
print(Matrix)

#visualizing correlation matrix of numeric variables
sns.heatmap(Matrix, annot=True)
plt.title('Correlation matrix for numeric features')
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show()

#copying df and saving it as df_numerized
df_numerized = df.copy()

#changing string variables into numeric
for col_name in df_numerized.columns:
    if (df_numerized[col_name].dtype=='object'):
        df_numerized[col_name]=df_numerized[col_name].astype('category')
        df_numerized[col_name]=df_numerized[col_name].cat.codes

print(df_numerized.head(5))

#correlation matrix for all variables
MatrixF = df_numerized.corr(method="pearson", numeric_only=True)
print(MatrixF)
sns.heatmap(MatrixF, annot=True)
plt.title('Correlation matrix for all features')
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show()

#sorted matrix to find high correlated variables
MatrixF = df_numerized.corr(method="pearson", numeric_only=True)
Matrix_pairs = MatrixF.unstack()
print(Matrix_pairs)
sorted_pairs= Matrix_pairs.sort_values() #sorting correlation values
print(sorted_pairs)
high_corr = sorted_pairs[(sorted_pairs) >0.5] #displaying only high correlated pairs
print(high_corr)




