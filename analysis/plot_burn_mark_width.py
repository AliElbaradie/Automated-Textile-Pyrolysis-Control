import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# Function to convert the custom time format to a datetime object
def convert_to_datetime(custom_time):
    return datetime.strptime(custom_time, '%H_%M_%S_%f')


# Function to process the lines and split into columns
def process_line(line, start_time):
    # Split the line by ';'
    part1, rest = line.split(';', 1)
    # Split the rest by ',' (we only need the part before the ',')
    part2, _ = rest.split(',', 1)
    # Convert the first part to datetime
    current_time = convert_to_datetime(part1)
    # Calculate the time difference
    time_diff = current_time - start_time
    # Convert the time difference to total seconds for plotting
    total_seconds = time_diff.total_seconds()
    return total_seconds, part2


# Read the input file and write to the output CSV file, also prepare data for plotting
def convert_text_to_csv_and_plot(input_file, output_file):
    times = []
    values = []

    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        # Write the header row
        csv_writer.writerow(['RelativeTime', 'Value'])

        # Read all lines from the input file
        lines = infile.readlines()

        if not lines:
            return

        # Get the start time from the first line
        first_line = lines[0].strip()
        start_time_str, _ = first_line.split(';', 1)
        start_time = convert_to_datetime(start_time_str)

        # Process each line
        for line in lines:
            # Remove any surrounding whitespace or newline characters
            line = line.strip()
            if line:
                # Process the line
                relative_time, value = process_line(line, start_time)
                # Multiply the value by 1/14 before appending
                adjusted_value = float(value) * (1 / 14)
                # Write to CSV
                csv_writer.writerow([relative_time, adjusted_value])
                # Collect data for plotting
                times.append(relative_time)
                values.append(adjusted_value)

    # Calculate the average value
    average_value = sum(values) / len(values)
    constant_value = 190 * (1 / 14)

    # Plotting the data
    plt.figure(figsize=(10, 6))
    plt.plot(times, values, marker='.', linestyle='-', label='x(t)')
    plt.axhline(y=average_value, color='r', linestyle='--', label=f'x̄(t) = {average_value:.2f} mm')
    plt.axhline(y=constant_value, color='g', linestyle=':', label='w(t) = 13,57 mm (190 Pixel)')
    plt.title('Verlauf der Regelgröße bei T = 500°C', fontsize=20)
    plt.xlabel('Zeit (Sekunden)', fontsize=18)
    plt.ylabel('Brandfleckdicke (mm)', fontsize=18)
    plt.legend(loc='lower left', fontsize=16)
    plt.grid(True)
    plt.show()


# Example usage
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.csv'  # Replace with your desired output file path
convert_text_to_csv_and_plot(input_file, output_file)
