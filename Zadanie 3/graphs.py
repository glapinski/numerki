import matplotlib.pyplot as plt


def graph(a, b, arguments, values, file_arguments, calculated_file_values, i_arguments, i_values):
    plt.plot(arguments, values, color='r', label='Funkcja interpolowana')
    plt.plot(i_arguments, i_values, color='g', label='Funkcja interpolacyjna')
    plt.scatter(file_arguments, calculated_file_values, c='b', label='Podane wezly')
    plt.legend()
    plt.title("Wykresy funkcji interpolowanej i interpolacyjnej")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim(a, b)
    plt.show()