# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image

# Read and glance a one-year-data (you need to provide the related file path where your files saved)
year_2000 = pd.read_csv('data/yob2000.txt')
# year_2000.head(10)
# year_2000.info()

# Create a function to read the txt file for a selected year
def parse_dataset(year):
    path = f'data/yob{year}.txt'
    df = pd.read_csv(path, names = ['name', 'gender', 'frequency'])
    return df

# Combine yearly datasets in a for loop and add year info into the dataset
# Since we are interested in data from 2000 and later, we can identify start_year as 2000 and end_year as 2024
df = pd.DataFrame(columns= ['name', 'gender', 'frequency'])
start_year = 2000
end_year = 2024

for year in range(start_year, end_year):
    df_temp = parse_dataset(year)
    df_temp['year'] = year
    df = pd.concat([df, df_temp])

df['year'] = df['year'].astype(int)

# Glance at the new combined dataset
# df.sample(15)

# Unify names from all years
name_data = df.groupby('name')['frequency'].sum().reset_index(name = 'total')

# Add an id column to use it in further steps
name_data['id'] = name_data.index

# Append a name k times (k = name's total number) in a list
name_list = []

for item in name_data['id']:
    rep_num = name_data['total'].values[item]
    for k in range(rep_num):
        name_list.append(name_data['name'].values[item])

name_list = pd.DataFrame(name_list, columns= ['names'])

# print (f'There are {len(name_list)} names in the combination of all names.')

# Convert DataFrame to a string by separating with a space
name_text = name_list['names'].str.cat(sep= ' ')

# Create a mask from the saved png
usa_mask = np.array(Image.open("./data/usa_map.png"))

# Create and generate a wordcloud
wordcloud = WordCloud(max_font_size= 300, # maximum font size for the largest word
                      min_font_size= 40, # smallest font size to use
                      background_color= 'black', # background color for the wordcloud image
                      colormap= 'rainbow', # Matplotlib colormap to randomly draw colors from for each word
                      mask= usa_mask, # mask for using an image
                      contour_width= 9, # if there is a mask, draw the mask contour (border)
                      contour_color= 'white', # mask contour (border) color
                      collocations= False # whether to include collocations (bigrams) of two words
                     ).generate(name_text)


# Plot the wordcloud
plt.figure(figsize=[25,25]) # set the size of wordcloud
plt.imshow(wordcloud, interpolation= 'bilinear') # display the generated wordcloud
plt.axis('off') # not show the axis of plot
plt.show()