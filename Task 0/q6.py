import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Processed_student_performance.csv")
student = "Student"
final_score = "Final_Score"
hours = "Hours_Studied"


#Bar chart
plt.figure(figsize=(10, 6))
plt.bar(df[final_score], df[student], color="blue", edgecolor="black")
plt.title("Student vs final scores", fontsize=14, fontweight="bold")
plt.xlabel("Student Name", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.tight_layout()
plt.savefig("final_scores.png", dpi=300)
plt.close()


#Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(
    df[hours], 
    df[final_score], 
    color="lightblue", 
    edgecolor="black"
)
plt.title("Hours Studied vs. Final Score", fontsize=14, fontweight="bold")
plt.xlabel("Hours Studied", fontsize=12)
plt.ylabel("Final Score", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("study_vs_score.png", dpi=300)
plt.close()


# --- 3. Histogram: Distribution of final scores ---
plt.figure(figsize=(10, 6))
plt.hist(
    df[final_score],
    bins=10,
    color="lightblue",
    edgecolor="black",
    rwidth=0.9,
)
plt.title("Distribution of Final Scores", fontsize=14, fontweight="bold")
plt.xlabel("Final Score Range", fontsize=12)
plt.ylabel("Number of Students (Frequency)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("score_distribution.png", dpi=300)
plt.close()


#Custom: box plot
plt.figure(figsize=(10, 6))
plt.boxplot(
    df[final_score], 
    vert=False, 
    patch_artist=True, 
)

plt.title('Box plot of Final Scores')
plt.xlabel('Final Score')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('custom_plot.png')
plt.close()

