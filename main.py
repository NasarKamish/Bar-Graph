import matplotlib.pyplot as plt

test_scores = [12,99,65,85,42]
test_names = ["Andy", "Martin", "Zahara", "Vuyo","Ziyaad" ]
pos_x = [k for k, _ in enumerate(test_names)]

plt.bar(pos_x, test_scores, color="Blue")
plt.xlabel("names")
plt.ylabel("Marks(%)")
plt.title("Python Marks for 5 students")
plt.xticks(pos_x, test_names)
plt.show()
