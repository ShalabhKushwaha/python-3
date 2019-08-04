from bokeh.plotting import figure, output_file, show

output_file("square.html")
p = figure(plot_width=400, plot_height=400)
p.square([1, 2, 3, 4, 10], [2, 9, 6, 12, 8], size=30, color='olive')
show(p)
