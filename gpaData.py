import pandas as pd
df = pd.read_csv("https://waf.cs.illinois.edu/discovery/gpa.csv")


df_removedup = df.groupby(['Year', 'Term', 'YearTerm','Subject','Number','Course Title','Primary Instructor']).agg(Aplus = ('A+', 'sum'), A=('A', 'sum'), Aminus = ('A-', 'sum'), Bplus = ('B+', 'sum'), B = ('B', 'sum'), Bminus = ('B-', 'sum'), Cplus = ('C+', 'sum'), C = ('C', 'sum'), Cminus = ('C-', 'sum'), Dplus = ('D+', 'sum'), D = ('D', 'sum'), Dminus = ('D-', 'sum'), F = ('F', 'sum'), W = ('W', 'sum')).reset_index()  
df_removedup.to_csv('output.csv')