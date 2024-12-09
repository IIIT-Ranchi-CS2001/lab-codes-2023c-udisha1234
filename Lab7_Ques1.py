# Show party wise seat share for following results of the Assembly Elections 2023 in
# Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached ( show the percentage seat share on each wedge )
# Two pie charts as subplots on the same figure object
# As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
# Madhya Pradesh
# BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
# Rajasthan
# INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)


#---------------------------------------CODE------------------------------------------

import matplotlib.pyplot as plt

# Data for Madhya Pradesh
mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]
mp_total_seats = sum(mp_seats)
mp_percentages = [round((seats / mp_total_seats) * 100, 1) for seats in mp_seats]

# Data for Rajasthan
rj_parties = ['INC', 'BJP', 'BSP', 'Others']
rj_seats = [69, 115, 2, 13]
rj_total_seats = sum(rj_seats)
rj_percentages = [round((seats / rj_total_seats) * 100, 1) for seats in rj_seats]

mp_explode = [0.1 if seats == max(mp_seats) else 0 for seats in mp_seats]
rj_explode = [0.1 if seats == max(rj_seats) else 0 for seats in rj_seats]

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

axes[0].pie(mp_percentages, labels=[f"{party} {perc}%" for party, perc in zip(mp_parties, mp_percentages)],
            explode=mp_explode, autopct='%1.1f%%', startangle=90)
axes[0].set_title("Madhya Pradesh Assembly Elections 2023")

axes[1].pie(rj_percentages, labels=[f"{party} {perc}%" for party, perc in zip(rj_parties, rj_percentages)],
            explode=rj_explode, autopct='%1.1f%%', startangle=90)
axes[1].set_title("Rajasthan Assembly Elections 2023")

plt.tight_layout()

plt.show()

fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.35
indices = range(len(mp_parties))

ax.bar(indices, mp_seats, bar_width, label='Madhya Pradesh', color='blue', alpha=0.7)
ax.bar([i + bar_width for i in indices], rj_seats, bar_width, label='Rajasthan', color='orange', alpha=0.7)

ax.set_xlabel('Parties')
ax.set_ylabel('Seats Won')
ax.set_title('Assembly Elections 2023: Seat Distribution')
ax.set_xticks([i + bar_width / 2 for i in indices])
ax.set_xticklabels(mp_parties)
ax.legend()

# Show the bar chart
plt.tight_layout()
plt.show()
