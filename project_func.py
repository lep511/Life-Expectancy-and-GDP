import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns


def labeled_scatter(df, year, save=False):
    
    xtick = np.arange(0, 20, 2.5)
    ytick = range(45, 85, 5)
    xlabel = "GDP (trillions of USD)"
    ylabel = "Life expectancy at birth (years)"
    
    plt.figure(figsize=(12, 7))
    data = df[df.Year == year].reset_index().copy()
    data["GDP_d"] = data.GDP / (10 ** 12)

    sns.scatterplot(data=data, x="GDP_d", 
                    y="Life expectancy at birth (years)",
                    hue="Country",
                    legend=False,
                    s=120
    )

    plt.xlabel(xlabel), plt.ylabel(ylabel) 
    plt.xticks(xtick), plt.yticks(ytick)
    plt.title("GDP and Life expectancy at birth (years) in {}".format(year), 
              fontsize=15)
    
    for line in range(0,data.shape[0]):
        plt.text(data.GDP_d[line]+0.2, 
                data["Life expectancy at birth (years)"][line]-0.6, 
                data.Country[line], 
                horizontalalignment='left', 
                size='medium', 
                color='black', weight='light'
    )
    plt.xlim(-1, 20)
    plt.ylim(42,84)
    plt.savefig("video/imag_"+str(year)) if save else plt.show()
    
    return


def fill_under_lines(ax=None, alpha=.2, **kwargs):
    if ax is None:
        ax = plt.gca()
    for line in ax.lines:
        x, y = line.get_xydata().T
        ax.fill_between(x, 0, y, color=line.get_color(), alpha=alpha, **kwargs)
        

def compare_plots(df, country):
    
    sns.set_style("white")
    sns.set_context("notebook", rc={"lines.linewidth": 1.2})
    
    data = df[df.Country == country]
    fig, ax = plt.subplots(1, 2, sharey=False, figsize=(16, 5))
    
    ax[0] = sns.lineplot(
        data=data, x="Year", y="GDP", palette="Blues", ax=ax[0]
    )
        
    fill_under_lines(ax[0])
    xlab = [2000, 2005, 2010, 2015]
    func_y = ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y/10 ** 9) + ' B')
    
    ax[0].yaxis.set_major_formatter(func_y)
    ax[0].set_xlabel("Years")
    ax[0].set_ylabel("GDP (billions of USD)")
    ax[0].set_title("Gross domestic product", fontsize=13)
    ax[0].set_xticks(xlab)
    ax[0].set_xticklabels(xlab)
    ax[0].set_xlim(2000, 2015)
    top = ax[0].set_ylim()[1]
    ax[0].set_ylim(2000, top)
    ax[0].grid(color="#EEEEEE")
    ax[0].xaxis.grid(False)
    sns.despine(ax=ax[0], left=True, bottom=True)
    
    fig.suptitle('{}'.format(country), fontsize=16)
    
    ax[1] = sns.lineplot(
        data=data, x="Year", y="Life expectancy at birth (years)", palette="Blues", ax=ax[1]
    )
    ax[1].set_xlim(2000, 2015)
    ax[1].set_ylim(40, 90)
    fill_under_lines(ax[1])
    ax[1].grid(color="#EEEEEE")
    ax[1].xaxis.grid(False)
    sns.despine(ax=ax[1], left=True, bottom=True)
    ax[1].set_xlabel("Years")
    ax[1].set_ylabel("Life expectancy at birth (years)")
    ax[1].set_title("Life expectancy at birth", fontsize=13)
    ax[1].set_xticks(xlab)
    sns.despine(ax=ax[1], left=True, bottom=True)
    
    return plt.show()