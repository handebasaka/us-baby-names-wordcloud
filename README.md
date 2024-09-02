## Creating a Wordcloud with US Baby Names

WordCloud is a great way of displaying word frequency. We can visualize and highlight the text-based data by customizing it to fit our needs. In the notebook below, we will create a word cloud to analyze baby names in the USA to see trending baby names from 2000.

**Dataset:** The US authorities have registered the names of all US citizens born since 1880. The record is publicly available. For data protection reasons, only names used at least 5 times are listed in the data record. We will download the data from [here](https://www.ssa.gov/oact/babynames/limits.html) and take the "National data" dataset.

To get started making a word cloud in Python, we will need some packages below:
- `pandas`: It is a data analysis and manipulation library that provides data structures and tools.
- `numpy`: It is a numerical computing library that provides support for large, multi-dimensional arrays and mathematical functions.
- `matplotlib.pyplot`: It is a plotting library for creating visualizations in Python.
- `wordcloud`: It provides functionality to create word clouds, visual representations of text data.
- `PIL, Image`: It is the Python Imaging Library, which provides image processing capabilities.

Since in the original dataset, there is no header, we need to add appropriate headers while reading txt files. So, it can look like below:

| # | Column | Dtype | Description |
| ---- | ---- | ---- | ---- |
| 0 | `name` | int64 | name |
| 1 | `gender` | int64 | gender - `F`: Female, `M`: Male |
| 2 | `frequency` | int64 | frequency of the name in that year  |


## Goals
- The goal of this project is to create a `WordCloud` to visualize and analyze trending baby names in the USA from the year 2000, highlighting the most popular names and their frequency in a visually engaging way. This will help us identify naming trends over the years using publicly available data from the Social Security Administration.

**Since the size of the dataset runtime may take a few minutes.*

## Tools and Technologies Used
`Python`

`Pandas` and `Numpy` for data manipulation 

`Matplotlib` and `WordCloud` for data visualization

## How to Run
clone:
```sh
git clone https://github.com/handebasaka/handebasaka
```
open the solution file:
```bash
cd handebasaka/us-baby-names-wordcloud
```
run python script:
```bash
python3 us-baby-names-wordcloud.py
```
