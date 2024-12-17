import matplotlib.pyplot as plt

def plot_kinetics(product_names, product_moles):
    """
    Plots the product distribution from the reactions.

    Parameters:
    - product_names (list): List of product names.
    - product_moles (list): Corresponding moles of products.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(product_names, product_moles, color='skyblue')
    plt.xlabel("Reaction Products")
    plt.ylabel("Moles Produced")
    plt.title("Reaction Product Distribution")
    plt.show()
