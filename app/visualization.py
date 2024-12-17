import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def animate_reactions_bar(reaction_data, total_time):
    """
    Animates the reaction product formation over time as a bar chart.
    """
    products = list(reaction_data.keys())
    max_moles = [reaction_data[product]['moles'] for product in products]
    num_steps = 100
    time_steps = np.linspace(0, total_time, num_steps)
    moles_over_time = [
        [mole * (t / total_time) for t in time_steps] for mole in max_moles
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(products, [0] * len(products), color="skyblue")
    ax.set_ylim(0, max(max_moles) * 1.2)
    ax.set_title("Reaction Product Formation Over Time (Bar Chart)", fontsize=16)
    ax.set_xlabel("Products", fontsize=14)
    ax.set_ylabel("Moles", fontsize=14)

    def update(frame):
        for bar, new_height in zip(bars, [m[frame] for m in moles_over_time]):
            bar.set_height(new_height)
        return bars

    anim = FuncAnimation(fig, update, frames=num_steps, blit=False, interval=50)
    plt.show()

def animate_reactions_line(reaction_data, total_time):
    """
    Animates the reaction product formation over time as a line graph.
    """
    products = list(reaction_data.keys())
    max_moles = [reaction_data[product]['moles'] for product in products]
    num_steps = 100
    time_steps = np.linspace(0, total_time, num_steps)
    moles_over_time = [
        [mole * (t / total_time) for t in time_steps] for mole in max_moles
    ]

    fig, ax = plt.subplots(figsize=(10, 6))
    lines = []
    for product in products:
        line, = ax.plot([], [], label=product)
        lines.append(line)

    ax.set_xlim(0, total_time)
    ax.set_ylim(0, max(max_moles) * 1.2)
    ax.set_title("Reaction Product Formation Over Time (Line Graph)", fontsize=16)
    ax.set_xlabel("Time (s)", fontsize=14)
    ax.set_ylabel("Moles", fontsize=14)
    ax.legend(loc="upper left")

    def update(frame):
        for line, moles in zip(lines, moles_over_time):
            line.set_data(time_steps[:frame + 1], moles[:frame + 1])
        return lines

    anim = FuncAnimation(fig, update, frames=num_steps, blit=False, interval=50)
    plt.show()
