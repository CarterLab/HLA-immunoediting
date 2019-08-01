def benjamini_fdr(list_values):
    '''
    Given a list of lists: [[thing tested, p-value]...]
        - Performs Benjamini & Hochberg FDR correction
    Returns same dataframe with adjusted p-values
    '''
    list_values = sorted(list_values, key=lambda x: x[1], reverse=False)
    total = len(list_values)
    for i in range(len(list_values)):
        rank = i+1
        new_pval = total/rank*(list_values[i][1])
        list_values[i][1] = min(new_pval, 1)
        
    return list_values