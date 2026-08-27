from heapq import heapreplace
import numpy as np

hours_studied = np.array([5.9, 3.6, 6.5, 5.4, 1.2])
attendance = np.array([100, 85, 73, 73, 74])
previous_scores = np.array([52, 74, 49, 78, 77])
final_scores = np.array([75, 47, 89, 50, 35])

print("Hours studied shape: ",hours_studied.shape)
print("Hours studied data type: ",hours_studied.dtype)
print("Attendance shape: ",attendance.shape)
print("Attendance data type: ",attendance.dtype)
print("Previous scores shape: ",previous_scores.shape)
print("Previous scores data type: ",previous_scores.dtype)
print("Final scores shape: ",final_scores.shape)
print("Final scores data type: ",final_scores.dtype)

print("Mean: " + str(np.mean(final_scores)))
print("Max: "+str(np.max(final_scores)) )
print("Min: "+str(np.min(final_scores)) )
new_score=final_scores+5
print("New score: ",new_score)
atleast_seventyfive= final_scores>=75
print("Boolean_array: ", atleast_seventyfive)
print("Scores above 75: ",final_scores[atleast_seventyfive])
