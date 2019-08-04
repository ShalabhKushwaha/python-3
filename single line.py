from bokeh.plotting import figure, output_file, show
output_file("single line.html")
p = figure(plot_width = 900, plot_height = 900)
p.line([1, 2, 3, 4], [4,6,2,13,9], line_width = 1.9)
show(p)