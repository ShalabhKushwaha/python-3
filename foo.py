# import modules 
from bokeh.plotting import figure, output_file, show

# output to notebook 
output_file("output.html")

# create figure 
p = figure(plot_width=400, plot_height=400)

# add a circle renderer with 
# size, color and alpha 
p.line([1, 2, 3, 4, 5], [4, 7, 1, 6, 3])

# show the results 
show(p)
