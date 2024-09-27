import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read the data from the file
    file_path = 'output.txt'  # Replace with your file path
    time = []
    system_output = []
    controller_output = []

    with open(file_path, 'r') as file:
        # Skip the header
        next(file)
        # Read the data
        for line in file:
            values = line.split()
            time.append(float(values[0]))
            system_output.append(float(values[1]))
            controller_output.append(float(values[2]))

    # Create a figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Plot System Output
    ax1.plot(time, system_output, label='System Output', marker='.', color='b')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('System Output')
    ax1.set_title('System Output vs. Time')
    ax1.legend()
    ax1.grid(True)

    # Plot Controller Output
    ax2.plot(time, controller_output, label='Controller Output', marker='.', color='r')
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Controller Output')
    ax2.set_title('Controller Output vs. Time')
    ax2.legend()
    ax2.grid(True)

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plot
    plt.show()
