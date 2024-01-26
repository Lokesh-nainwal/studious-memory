# import python libraries
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd 
# import csv file
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
# Function to update the plot 
def update_plot():
    selected_plot = plot_dropdown.get()
    
    if selected_plot == 'Gender Distribution':
        ax = sns.countplot(x='Gender', data=df)
        ax.set_title('Gender Distribution')
        ax.set_xlabel('Gender')
        ax.set_ylabel('Count')
        for bars in ax.containers:
            ax.bar_label(bars)
    elif selected_plot == 'Sales by Gender':
        sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
        sns.barplot(x='Gender', y='Amount', data=sales_gen)
        plt.title('Sales by Gender')
        plt.xlabel('Gender')
        plt.ylabel('Total Sales')
    
    # Add more elif conditions for other plots
    
    canvas.draw()

# Create the main window
root = tk.Tk()
root.title('Diwali Sales Data Visualization')

# Create a frame for the controls
controls_frame = ttk.Frame(root)
controls_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Dropdown for selecting the plot
plot_label = ttk.Label(controls_frame, text='Select Plot:')
plot_label.grid(row=0, column=0, padx=25, pady=20, sticky=tk.W)
plot_options = ['Gender Distribution', 'Sales by Gender']  # Add more options as needed
plot_dropdown = ttk.Combobox(controls_frame, values=plot_options)
plot_dropdown.grid(row=0, column=1, padx=25, pady=20, sticky=tk.W)
plot_dropdown.set(plot_options[0])

# Button to update the plot
update_button = ttk.Button(controls_frame, text='Update Plot', command=update_plot)
update_button.grid(row=0, column=2, padx=20, pady=20)

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Initialize a figure and axis for the plot
fig, ax = plt.subplots(figsize=(15, 12))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Call the update_plot function initially to display the default plot
update_plot()

# Start the GUI event loop
root.mainloop()
