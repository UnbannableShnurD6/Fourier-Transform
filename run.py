import numpy as np
import matplotlib.pyplot as plt


def fourier_transform_impl(y_array):
    y_array = np.asarray(y_array)
    fourier_samples_number = y_array.shape[0]
    range_to_samples_num = np.arange(fourier_samples_number)
    reshaped_range_to_samples_num = range_to_samples_num.reshape((fourier_samples_number, 1))
    return np.dot(np.exp(np.pi * -2j * reshaped_range_to_samples_num * range_to_samples_num / fourier_samples_number), y_array)


def fourier_transform(x_array, y_array, use_lib_impl=False):
    if use_lib_impl:
        transformed_data = np.fft.fft(y_array)
    else:
        transformed_data = fourier_transform_impl(y_array)

    sample_rate = x_array[1] - x_array[0]
    fourier_samples_number = y_array.size

    frequency = 1 / sample_rate
    f = np.linspace(0, frequency, fourier_samples_number)

    figure = plt.figure()
    ax = figure.add_subplot()
    ax.set_title(f"Сигнал после преобразования Фурье{' (библиотечного)' if use_lib_impl else ''}:")
    ax.set_xlabel("Частота (Гц)")
    ax.set_ylabel("Амплитуда")
    normalization_factor = 1 / fourier_samples_number
    right_border = fourier_samples_number // 2
    ax.bar(f[:right_border], np.abs(transformed_data)[:right_border] * normalization_factor, width=1.5)
    plt.show()
    figure.savefig(f"{'fourier_transformed_signal_by_lib.png' if use_lib_impl else 'fourier_transformed_signal.png'}")


def generate_signal(constants):
    samples_number = 800
    x_array = np.linspace(0, 0.5, samples_number)
    y_array = 0
    for constant in constants:
        y_array += np.sin(constant * 2 * np.pi * x_array)

    figure = plt.figure()
    ax = figure.add_subplot()
    ax.plot(x_array, y_array)
    ax.set_title("Сгенерированный сигнал")
    ax.set_xlabel("Время (с)")
    ax.set_ylabel("Амплитуда")
    plt.show()
    figure.savefig("generated_signal.png")

    return y_array, x_array


print("Доброе пожаловать в преобразование Фурье!")
constants = []
additional_constant = input("Введите константу (лучше что-нибудь > 7), на основе которой будет построен сигнал: (например, 10)")
while additional_constant != "":
    constants.append(int(additional_constant))
    additional_constant = input("Введите дополнительную константу, или нажмите Enter чтобы закончить:")

y_array, x_array = generate_signal(constants)
fourier_transform(x_array, y_array, use_lib_impl=False)
fourier_transform(x_array, y_array, use_lib_impl=True)
print("Сгенерированный сигнал находится в файле generated_signal.png")
print("Результаты находятся в файлах fourier_transformed_signal.png и fourier_transformed_signal_by_lib.png")