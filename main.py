from app.calculations import simulate_reactions
from app.visualization import animate_reactions_bar, animate_reactions_line

def main():
    # Simulation parameters
    current = 10  # Amperes
    time = 3600  # 1 hour in seconds
    catalyst = "Cu"  # Catalyst used

    # Run the simulation
    reaction_results = simulate_reactions(current, time, catalyst)

    # Choose the visualization
    print("Choose visualization type:")
    print("1: Bar Chart")
    print("2: Line Graph")
    print("3: Both")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        animate_reactions_bar(reaction_results, time)
    elif choice == "2":
        animate_reactions_line(reaction_results, time)
    elif choice == "3":
        animate_reactions_bar(reaction_results, time)
        animate_reactions_line(reaction_results, time)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
