import matplotlib.pyplot as plt

def generate_bar_chart(labels, values , country):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(f'Población por año en {country}')
    ax.set_xlabel('Año')
    ax.set_ylabel('Población')
    plt.show()
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

