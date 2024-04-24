

import csv
import numpy as np
import matplotlib.pyplot as plot

def mean_and_SD_2020_2024_all_data():
    all_data_2020 = tuple()
    all_data_2024 = tuple()
    with open('2020input1.csv', 'r') as file2020:
        reader = csv.reader(file2020, delimiter=" " )
        rows = [[int(x) for x in row if len(x) > 0] for row in reader]        
        data_2020 = []
        for lower_range, upper_range, frequency in rows:
            mid_point = (lower_range + upper_range) / 2
            data_2020.extend([mid_point] * frequency)
        mean_2020 = np.mean(data_2020)
        std_dev_2020 = np.sqrt(np.var(data_2020))
        all_data_2020 = (mean_2020, std_dev_2020, data_2020)

    with open('2024input1.csv', 'r') as file2024:
        reader = csv.reader(file2024, delimiter=' ')
        data_2024 = [int(num) for row in reader for num in row if len(num) > 0]
        mean_2024 = np.mean(data_2024)
        std_dev_2024 = np.sqrt(np.var(data_2024))
        all_data_2024 = (mean_2024, std_dev_2024, data_2024)
    return all_data_2020, all_data_2024

def assignment_func():
    all_data_2020, all_data_2024 = mean_and_SD_2020_2024_all_data()
    mean_2020, std_dev_2020, data_2020 = all_data_2020[0], all_data_2020[1], all_data_2020[2]
    mean_2024, std_dev_2024, data_2024 = all_data_2024[0], all_data_2024[1], all_data_2024[2]

    v_value = mean_2024 - mean_2020
    
    plot.figure(figsize=(10, 5))

    plot.subplot(1, 1, 1)
    plot.hist(data_2020, bins=30, color='blue', alpha=0.5, label='2020input1')
    plot.hist(data_2024, bins=30, color='red', alpha=0.5, label='2024input1')
    plot.title('Histogram(ID 23031501)')
    plot.xlabel('Data Value')
    plot.ylabel('Data Frequency')
    plot.legend()

    plot.text(0.05, 0.95, f'Student\'s id: 23031501', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.text(0.05, 0.90, f'Mean of 2020: {mean_2020:.2f}', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.text(0.05, 0.85, f'Mean of 2024: {mean_2024:.2f}', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.text(0.05, 0.80, f'Standard Deviation of 2020: {std_dev_2020:.2f}', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.text(0.05, 0.75, f'Standard Deviation of 2024: {std_dev_2024:.2f}', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.text(0.05, 0.70, f'V Value: {v_value:.2f}', ha='left', va='top', color='black', transform=plot.gca().transAxes)
    plot.savefig('23031501.png')
    plot.show()
            

if __name__ == "__main__":
    assignment_func()


