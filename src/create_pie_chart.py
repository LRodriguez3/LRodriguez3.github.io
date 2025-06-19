import matplotlib.pyplot as plt


def plot_pie_chart(list_cat:list):

    # Updated data for the pie chart with the new category
    labels = list(map(lambda x: x["cat"], list_cat))
    sizes = list(map(lambda x: x["size"], list_cat))
    colors = list(map(lambda x: x["color"], list_cat))

    # Create the updated pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Save the updated pie chart to a file
    updated_pie_chart_path = '../images/cat_pie_chart.png'
    plt.savefig(updated_pie_chart_path)


if __name__ == "__main__":

    list_cat = [
        {"cat": "Data Science", "size":25, "color":"#ff9999"},
        {"cat": "Data Engineering", "size":30, "color":"#66b3ff"},
        {"cat": "Data Analysis", "size":15, "color":"#99ff99"},
        {"cat": "ML Engineering", "size":30, "color":"#ffcc99"},
    ]

    plot_pie_chart(list_cat=list_cat)