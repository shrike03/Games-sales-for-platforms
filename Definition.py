import pandas as pd
import matplotlib.pyplot as plt 

# Function for grouping and filtering data based on a category and aggregation key
def grouping(df_org,category, group_key,sort_values,asc,value_type,display_mode,n_plt,n_disp):
    # Group the original DataFrame by 'Platform' and sum the selected values
    platform = df_org.groupby(by = 'Platform')[group_key].sum().round(2)
    # Select top or bottom N platforms based on total value
    if value_type == 'head':
         top_platform = platform.sort_values(ascending=False).head(n_plt)
    elif value_type == 'tail':
         top_platform = platform.sort_values(ascending=False).tail(n_plt)
    else:
        print('Write correct value to select sells on platform: tail or head')

     # Filter the original DataFrame to include only selected platforms
    top_ind = top_platform.index.to_list()
    df_top_plt = df_org[df_org['Platform'].isin(top_ind)]
    # Group by the chosen category (e.g., Genre, Year, Publisher)
    grouping = df_top_plt.groupby(by=category)[group_key].sum().round(2)
    df_grouped = pd.DataFrame(grouping)
    # Sort the grouped DataFrame by selected column
    df_sorted = df_grouped.sort_values(by=sort_values, ascending=asc)
    # Return a portion or all of the sorted DataFrame
    if display_mode == 'head':
         return df_sorted.head(n_disp)
    elif display_mode == 'tail':
          return df_sorted.tail(n_disp)
    elif display_mode == 'all':
          return df_sorted
    else:
        print('Write correct value to display correct sorted dataframe: tail, head or all')
    
    
# Function to generate a chart from a pivot table
def chart(df,df_ind,df_col,df_val,df_agg,plt_kind,plt_size):
    # Create pivot table from input DataFrame
    pvt_tab=df.pivot_table(index=df_ind, columns=df_col, values=df_val,aggfunc=df_agg)
    # Plot the pivot table as a stacked or standard chart
    pvt_tab.plot(kind=plt_kind, stacked=True, figsize = plt_size)

# Function to calculate the percentage share of a region's sales in the total platform sales
def precentage_top(gs_df,gs_key,region_key,n_plt):
     # Group global sales by platform
     platform_global = gs_df.groupby(by = 'Platform')[gs_key].sum().round(2)
     # Select top N platforms
     top_platform = platform_global.sort_values(ascending=False).head(n_plt)
     top_list = top_platform.index.to_list()
     # Filter original DataFrame to only top platforms
     gs_platform = gs_df.loc[gs_df['Platform'].isin(top_list)]
     # Total global sales per platform
     gs_group = gs_platform.groupby(by='Platform')[gs_key].sum().round(2)
     # Sales in the selected region per platform
     region_group = gs_platform.groupby(by='Platform')[region_key].sum().round(2)
     # Calculate percentage of regional sales in global sales
     reg_precentage = region_group/gs_group

     return reg_precentage.round(2)*100

# Function to generate pie charts for each column in the given DataFrame
def many_chart_pie(df,plt_size,):
     for column in df.columns:
          plt.figure(figsize=plt_size)
          # Draw pie chart with labels and percentage display
          plt.pie(df[column], labels=df.index, autopct='%1.1f%%', textprops={'fontsize': 10})
          plt.title(f'Sales breakdown for {column} by region')
          plt.show()

