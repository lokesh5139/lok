
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(student_id, year):
    filename = f'{year}input{student_id}.csv'
    if year == 2020:
        return pd.read_csv(filename, delim_whitespace=True, header=None, names=['bin_start', 'bin_end', 'count'])
    elif year == 2024:
        df = pd.read_csv(filename, header=None, names=['grade'])
        df['grade'] = pd.to_numeric(df['grade'], errors='coerce')
        return df

def prepare_bins(df_2020):
    return pd.interval_range(start=df_2020['bin_start'].min(), end=df_2020['bin_end'].max(), periods=len(df_2020))

def bin_data(df, bins):
    return pd.cut(df['grade'], bins=[edge.left for edge in bins] + [bins[-1].right])

def calculate_statistics(df, weights=None):
    if weights is not None:
        mean_val = np.average(df, weights=weights)
        variance = np.sum((df - mean_val)**2 * weights) / weights.sum()
    else:
        mean_val = df.mean()
        variance = df.var()
    return mean_val, np.sqrt(variance)

def plot_histogram(bins, hist_2020, hist_2024, stats, student_id):
    plt.figure(figsize=(10, 6))
    bar_width = (bins[0].right - bins[0].left) / 3
    plt.bar(bins.mid - bar_width/2, hist_2020, width=bar_width, color='coral', alpha=0.8, label='2020 Exam Grades')
    plt.bar(bins.mid + bar_width/2, hist_2024, width=bar_width, color='deepskyblue', alpha=0.8, label='2024 Exam Grades')
    plt.text(0.05, 0.95, f'Mean (2020): {stats['mean_2020']:.2f}\nStd Dev (2020): {stats['std_2020']:.2f}\n'
             f'Mean (2024): {stats['mean_2024']:.2f}\nStd Dev (2024): {stats['std_2024']:.2f}\n'
             f'Value V (≥70 in 2024): {stats['v_value_2024']:.2f}%\nStudent ID: {student_id}',
             transform=plt.gca().transAxes, fontsize=9, verticalalignment='top', bbox=dict(boxstyle="round", alpha=0.5))
    plt.xlabel('Grade')
    plt.ylabel('Normalized Frequency')
    plt.title('Comparative Analysis of Exam Grades Distribution (2020 vs 2024)')
    plt.legend()
    plt.savefig(f'{student_id}.png')
    plt.close()

# Example function calls
df_2020 = load_data('1', 2020)
df_2024 = load_data('1', 2024)
bins = prepare_bins(df_2020)
df_2024['bins'] = bin_data(df_2024, bins)
hist_2020 = df_2020['count'] / df_2020['count'].sum()
hist_2024 = df_2024['bins'].value_counts(sort=False).reindex(bins, fill_value=0) / df_2024['bins'].value_counts(sort=False).sum()
mean_2020, std_2020 = calculate_statistics((df_2020['bin_start'] + df_2020['bin_end']) / 2, df_2020['count'])
mean_2024, std_2024 = calculate_statistics(df_2024['grade'])
v_value_2024 = (df_2024['grade'] >= 70).mean() * 100

stats = {
    'mean_2020': mean_2020,
    'std_2020': std_2020,
    'mean_2024': mean_2024,
    'std_2024': std_2024,
    'v_value_2024': v_value_2024
}

plot_histogram(bins, hist_2020, hist_2024, stats, '23031501')
