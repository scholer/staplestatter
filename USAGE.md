Using the cadnano plugin interface:
-------------------------------------

The plugin interface has two tabs in addition to the "Usage help" tab.

One control tab where you do the plotting, and another where you specify what to plot.
The former is the simplest: Press the "Process and plot!" button
to plot according to the directives provided in the "Specify plots" tab.
You can then save the plot or data if you'd like.

The "Specify plots" tab has a big text area, which is used to
specify how to analyze the design and how the result should be
plotted and/or printed.

The input format is in yaml. You will need to know a bit of yaml
as well as standard python datastructs to feel really comfortable
editing the input. However, even without prior knowledge, you
can probably figure out a lot by immitating and modifying the
examples.

The yaml input in the text area takes the form of a dict with keys:

`figure` : specify figure format (optional)

`statspecs` : a list of dicts, where each 'statspecs' dict specifies
a statistical analysis method, including how to plot and/or print the data/statistics.


A `statspec` dict in the `statspecs` list can contain the following elements:

- `scoremethod` : A way to score the design. See statutils.py.
- `scoremethod_kwargs` : This is passed to the scoremethod as **kwargs.
- `plot_frequencies` : Whether to plot frequency histogram, rather than individual items. Default=True.
- `plotspec` : a dict specifying how to plot the results of this scoring method.
- `printspec` : a dict specifynig how to output the results of this scoring method.

The plotspec dict can have the following elements:

- `plot_kwargs` : a dict which is passed to the plotting method (currently pyplot.vlines).
- `label` : What label to use for this plot. The label appears in e.g. the legend.
- `label_fmt` : can be used to automatically format the label.
- `xlabel` : label ON THE X-AXIS.
- `subplot` : subplot specification (where to plot the graph within the figure, as n-rows, n-cols, plot-number).
- `xlim` : two-item list of [xmin, xmax].
- `ylim` : two-item list of [ymin, ymax].
- `title` : What title to use for the plot.
- `title_fmt` : Can be used to automatically format the title.
- `legend` : dict. Will be passed as pyplot.legend(**legend)

The `printspec` element is currently just a kwargs dict, which gets passed to
`staplestatter.get_highest_scores()`.

Regarding scoremethod_kwargs: {margin: 0}

* 'margin' is currently only keyword argument. 
    This is set at a per-plot level. It is not used by all scoring methods.


If you want to plot statistics for multiple cadnano designs in the same figure, 
you can set the `figure.newfigure` option to `false`. 
This will re-use the old figure instead of creating a new figure every time you press "Process and plot!" button.
Now, just load the designs one by one, plotting each design with the "Process and plot!" button.


[refresh](USAGE.html)


