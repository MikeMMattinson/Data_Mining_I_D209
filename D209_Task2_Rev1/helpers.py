# helper functions

print('getFilename version: {}'.format('1.0'))
def getFilename(title: str, caption: str,
             sect='XX', ftype = 'PNG',
            course = 'D209', task = 'TASK1',
               subfolder='figures') -> str:
    """
    Construct a filename for given figure or table
    Input:
      title:
      sect:
      caption:
      ftype:
      course:
      task:
      subfolder:
    """
    temp = subfolder + '/'  # subfolder for tables and figures, default is 'fig'
    temp += course + '_'
    temp += task + '_'
    temp += sect + '_'
    temp += subfolder[0:3] + " " +caption + '_' #
    temp += title
    temp += '.' + ftype

    return temp.replace(' ','_').upper()


print('saveTable version: {}'.format('1.0'))
def saveTable(data, title: str, caption: str, 
              sect='XX',course='D209', 
              task='TASK1'):
    """
    Construct a filename for given figure or table
    Input:
      data:
      title:
      sect:
      caption:
      ftype:
      course:
      task:
      subfolder:
    """    
    # construct filename based on parameters
    f = getFilename(title=title, sect=sect, task=task, 
                caption=caption, ftype='CSV', 
                course=course, subfolder='tables')
    data.to_csv(f, index=True, header=True) # create .csv file
    display(data.head(4).T) # display dataframe head data translated for vertical readibility
    print('shape: {}'.format(data.shape)) # describe dataframe rows and cols
    print('Table saved to: {}'.format(f)) # feedback to notebook   
    
    
print('describeData version: {}'.format('1.0'))      
def describeData(data):
    """
    Describe a set of data as Continuous or Categorical
    Input:
      data: dataframe to be described
    """ 
    for idx, c in enumerate(data.columns):
        if data.dtypes[c] in ('float', 'int', 'int64'):
            print('\n{}. {} is numerical (CONTINUOUS) - type: {}.'.format(idx+1, c, data.dtypes[c]))
            if data.dtypes[c] in ('int', 'int64'):
                numbers = data[c].to_numpy()
                print('  Unique: {}'.format(get_unique_numbers(numbers)))
            if data.dtypes[c] in ('float', 'float64'):
                print('  Min: {:.3f}  Max: {:.3f}  Std: {:.3f}'.format(data[c].min(), data[c].max(),data[c].std()))
            
        elif data.dtypes[c] == bool:
            print('\n{}. {} is boolean (BINARY): {}.'.format(idx+1,c,data[c].unique()))
        else:
            print('\n{}. {} is categorical (CATEGORICAL): {}.'.format(idx+1,c,data[c].unique()))  

    
print('createScatter version: {}'.format('1.0'))
def createScatter(data,feature,target,c,edgecolor,title,caption,course,task):
    """
    Create and save a custom scatter plot fiugre
    Input:
    data: dataframe
    feature:
    target:
    c:
    edgecolor:
    title:
    caption:
    course:
    """
    import matplotlib.pyplot as plt
    
    # define a couple of plot variables
    title = title + ' ' + str(feature) + ' ' + str(target)
    
    # create fig,ax
    fig,ax = plt.subplots()
    ax.scatter(data[feature],data[target],c=c,edgecolor=edgecolor)
    
    # set title
    ax.set_title(title.upper(), fontsize=16)
    
    # create filename and save
    f=getFilename(title=title, caption=caption,
                  course=course, task=task,
                  ftype='PNG', subfolder='figures')
    plt.gcf().text(0, -.05, f, fontsize=14)
    fig.savefig(f, dpi=150, bbox_inches='tight') 
    print('Figure saved to: {}'.format(f)) # feedback to notebook
    
    
print('createBarplot version: {}'.format('1.1'))
def createBarplot(data,feature,target,title,caption,course,task):
    """
    Create and save a custom bar plot fiugre
    Input:
    feature: feature (Categorical)
    target: target (Numerical)
    title:
    caption:
    course:
    """
    import matplotlib.pyplot as plt
    fig,ax = plt.subplots()
    ax=data.groupby(feature).mean()[target].plot(kind='bar')
    title = title + ' ' + str(feature) + ' ' + str(target)
    ax.set_title(title.upper())
    ax.set_ylabel(('Ave. ' + target).upper())
    f=getFilename(title=title, caption=caption,
                  course=course, task=task,
                  ftype='PNG', subfolder='figures')
    plt.gcf().text(0, -.05, f, fontsize=14)
    fig.savefig(f, dpi=150, bbox_inches='tight') 
    print('Figure saved to: {}'.format(f)) # feedback to notebook
    
    

print('get_unique_numbers version: {}'.format('1.0'))    
def get_unique_numbers(numbers):
    """
    Input:
    numbers: array
    
    Ref: https://www.freecodecamp.org/news/python-unique-list-how-to-get-all-the-unique-values-in-a-list-or-array/
    """
    list_of_unique_numbers = []
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_of_unique_numbers.append(number)
    return list_of_unique_numbers


print('createCorrelationMatrix version: {}'.format('1.0'))
def createCorrelationMatrix(data,title,caption,course,task,highest):
    """
    Create and save custom correlation matrix (heatmap) plot
    Input:
    data: dataframe of corr matrix
    c:
    edgecolor:
    title:
    caption:
    course:
    """
    import matplotlib.pyplot as plt
    import seaborn as sns
    fig,ax = plt.subplots()
    sns.heatmap(data.corr(), annot=True, fmt='.1f', 
        cmap='RdBu', center=0, ax=ax)
    ax.set_title(title.upper())
    fig.set_size_inches(8, 5)
    f=getFilename(title=title, caption=caption,
                  course=course, task=task,
                  ftype='PNG', subfolder='figures')
    plt.gcf().text(0, -.05, f, fontsize=14)
    plt.gcf().text(0, -.1, 'Top ' + str(highest) + ' Correlations:', fontsize=14, 
              horizontalalignment='left', verticalalignment='top') 
    plt.gcf().text(.04, -.15, get_top_abs_correlations(data, n=highest).to_string(), 
              fontsize=14,horizontalalignment='left', verticalalignment='top') 
    fig.savefig(f, dpi=150, bbox_inches='tight') 
    print('Figure saved to: {}'.format(f)) # feedback to notebook
        

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]
        

print('createStackedHistogram version: {}'.format('1.0'))
def createStackedHistogram(data,feature,target,title,caption,course,task,bins=9,isCat=True):
    """
    Create and save a custom stacked histogram
    Input:
    data:
    feature: feature (Numerical)
    target: target (Yes/No)
    title:
    caption:
    course:
    task:
    bins:
    isCat: bool if target is cat, else num
    """
    import matplotlib.pyplot as plt
    import pandas as pd
    
    # create fig,ax
    fig,ax = plt.subplots()
    
    # define couple of plot variables
    if isCat==True:
        
        yes = data[data[target]=='yes'][feature]; yes_mean = yes.mean();
        no = data[data[target]=='no'][feature]; no_mean = no.mean()

    else:
        yes = data[data[target]==1][feature]; yes_mean = yes.mean();
        no = data[data[target]==0][feature]; no_mean = no.mean()   
        
    plt.hist([yes, no], bins=bins, stacked=True)
    title = title + ' ' + str(feature) + ' ' + str(target)
    
    # add legend
    ax.legend([str(target)+'= Yes',str(target)+'= No'])
    
    # add datatable
    b = pd.cut(data[feature], bins=bins) # create bins (b) of numeric feature
    ct = pd.crosstab(data[target], b)
    plt.gcf().text(0.1, -.05, ct.T.to_string(), fontsize=14,
            horizontalalignment='left', verticalalignment='top')
    
    # set min-max x and y limits
    ymin, ymax = ax.get_ylim()
    xmin, xmax = ax.get_xlim()
    
    # add title
    plt.title(title.upper(), fontsize=16)
    
    # axis labesl
    plt.xlabel(feature.upper())
    plt.ylabel(target.upper())
    
    # create group mean lines
    ax.axvline(yes_mean, color="blue", lw=2)  # yes mean
    ax.axvline(no_mean, color="orangered", lw=2)  # no mean
    #ax.text((xmax - xmin) / 2,
    #        (ymax - ymin) / 2,
    #        "Delta:\n" + str(round(abs(yes_mean - no_mean), 2)),
    #        bbox={"facecolor": "white"} )
    
    # add filename and save
    f=getFilename(title=title, caption=caption,
                  course=course, task=task,
                  ftype='PNG', subfolder='figures')
    plt.gcf().text(0, -.05, f, fontsize=14)
    fig.savefig(f, dpi=150, bbox_inches='tight') 
    print('Figure saved to: {}'.format(f)) # feedback to notebook
    