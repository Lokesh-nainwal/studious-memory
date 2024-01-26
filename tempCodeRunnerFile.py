# Dropdown for selecting the plot
plot_label = ttk.Label(controls_frame, text='Select Plot:')
plot_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
plot_options = ['Gender Distribution', 'Sales by Gender']  # Add more options as needed
plot_dropdown = ttk.Combobox(controls_frame, values=plot_options)
plot_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
plot_dropdown.set(plot_options[0])

# Button to update the plot
update_button = ttk.Button(controls_frame, text='Update Plot', command=update_plot)
update_button.grid(row=0, column=2, padx=10, pady=5)

# Create a frame for the plot
plot_frame = ttk.Frame(root)
plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Initialize a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 5))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Call the update_plot function initially to display the default plot
update_plot()

# Start the GUI event loop
root.mainloop()
