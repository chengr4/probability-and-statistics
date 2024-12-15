import matplotlib.pyplot as plt

# Remark: Not a good example of a Pareto chart

# Defect data
defect_data = {'a': 10, 'b': 35, 'c': 6, 'd': 15, 'e': 50, 'f': 4}

# Sort data by frequency in descending order
sorted_defects = sorted(defect_data.items(), key=lambda x: x[1], reverse=True)
defects, counts = zip(*sorted_defects)

# Cumulative percentage
cumulative_counts = [sum(counts[:i+1]) for i in range(len(counts))]
cumulative_percentage = [x / sum(counts) * 100 for x in cumulative_counts]

# Plotting
fig, ax1 = plt.subplots()

ax1.bar(defects, counts, color='C0')
ax1.set_xlabel('Defect Type')
ax1.set_ylabel('Frequency', color='C0')

ax2 = ax1.twinx()
ax2.plot(defects, cumulative_percentage, color='C1', marker='D', ms=7)
ax2.set_ylabel('Cumulative Percentage (%)', color='C1')
ax2.set_ylim(0, 100)

plt.title('Pareto Chart of Defect Types')
plt.show()