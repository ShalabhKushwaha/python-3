from bokeh.plotting  import figure, output_file, show
output_file('step line.html')
p = figure(plot_width = 400, plot_height = 400)
p.step([1,2,3,4,5],[6,7,2,4,5], line_width = 2, mode = 'center')
show(p)