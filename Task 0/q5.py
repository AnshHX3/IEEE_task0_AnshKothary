import pandas as pd

df = pd.read_csv('student_performance.csv')

print(df.head())
print("(Rows, Columns): ", df.shape)
print("Column names: ", df.columns)
print("Missing values: ",df.isna().sum())
print("Mean of final score: ",df['Final_Score'].mean())
print("Max: ",df['Final_Score'].max())
df['Improvement'] = df['Final_Score']-df['Previous_Score']
df_min_attendance = df[df['Attendance'] >= 80]
df_new = df_min_attendance.sort_values(by="Final_Score", ascending=False)
df_new.to_csv('Processed_student_performance.csv',index='False')