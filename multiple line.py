from bokeh.plotting import figure, output_file, show

output_file("multiple.html")
p = figure(plot_width=400, plot_height=400)
p.multi_line([[1, 2, 3, 4, 5], [12, 13, 45, 2]], [[3, 5, 7, 9], [17, 22, 3, 9]], line_width = 3 )
show(p)