import matplotlib.pyplot as plt
from Classnov import Novice
from Classexd import Experienced
from Classext import Expert

novice_a = Novice("Jack", 23, 3, None)
experienced_a = Experienced("Bond", 31, 6, None)
novice_b = Novice("Roy", 25, 4, None)
experienced_b = Experienced("Hunt", 36, 7, None)
expert = Expert("Iulia", 47, 13, None)
count_j = 0
count_b = 0
count_r = 0
count_h = 0
count_i = 0

for run_time in range(5):
    with open("Shooting_results_log", "a", encoding="utf-8") as f:
        shooters = [novice_a, experienced_b, novice_b, experienced_a, expert]
        for res in shooters:
            on_target = res.fire()
            f.write(res.name + ":" + "\n")
            f.write(str(res.age) + " " + "Տարեկան" + "," + " ")
            f.write("Փորձառություն" + " " + str(res.experience) + "(տարի)։" + "\t" + "\t")
            if on_target:
                if res.name == "Jack":
                    count_j += 1
                elif res.name == "Bond":
                    count_b += 1
                elif res.name == "Roy":
                    count_r += 1
                elif res.name == "Hunt":
                    count_h += 1
                elif res.name == "Iulia":
                    count_i += 1
                f.write("On target" + " " + "(Դիպուկ է:)" + "\n")
            else:
                f.write("Not on target" + " " + "(Շեղ է։)" + "\n")
        f.write("\n\n")

fig, ax = plt.subplots()
shooters = ["Jack", "Bond", "Roy", "Hunt", "Iulia"]
print("\n", "Jack =", count_j, "\n", "Bond =", count_b, "\n", "Roy =", count_r, "\n", "Hunt =", count_h, "\n",
      "Iulia =", count_i, "\n")
counts = [count_j, count_b, count_r, count_h, count_i]
bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange", "tab:purple"]
ax.bar(shooters, counts, color=bar_colors)

ax.set_ylabel("Shots on target")
ax.set_title("Results")
plt.plot(shooters, [1, 2, 3, 4, 5], color="None")
plt.show()
