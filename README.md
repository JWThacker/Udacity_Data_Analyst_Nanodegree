![Udacity Image](./img/data_analyst.png)

## Udacity - Data Analyst

This repository holds exercises and project necessary for me to complete the Data Analyst nanodegree by Udacity. There were five main modules/lessons to this module and each are completed using Python:

   - The Welcome module where info about the course is given as well what a Data Analyst does. (Project necessary for this module)

  - The Introduction to Data Analysis module where a survey topics including importing data, plotting data, assessing data and cleaning data etc were introduced. (Project necessary for this module)

  -  The Practical Statistics module/lesson where descriptive statistics, probability, various distributions and sampling distributions, various inferential statistics, regression/multiple regression/logistic regression and A/B testing were taught. A lot of this module was review for me, but A/B was new for me. In addition to learning these topics, we applied them in exercises using Python. Any exercises I found notable for this module can be found in the *practicalStats* directory. (Project necessary for this module)

  - The Data Wrangling/Cleaning module/lesson taught me how to gather data, assess data, clean data and then source data. I have had several of my friends/classmates ask me where I acquired my data-cleaning skills that I have applied in the classroom and a research meta-analysis; *this module* is where I learned my data-cleaning skills. (Project necessary for this module)

  - The Data Visualization module/lesson taught me the fundamentals of how to make lucid and informative visualizations. This module and the previous module (data wrangling/cleaning) were my favorite modules. (Project necessary for this module)

All projects for this module will be explained in the *Projects* section.

## Projects

### Project 1

   1. In this project, I analyzed data consisting of local and global temperatures and compared temperature data for where I live (near Atlanta) to the overall global trend. In this project I used Python and SQL to achieve each task. For the project I was tasked with:

      - Extracting the data from a database using a couple of SQL queries.
      - Calculate a moving average.
      - Create a line chart.

### Project 2

   2. This project was a bit open-ended. The goal was to investigate one of Udacity's datasets to answer interesting questions about it. In the notebook for this project you can find the questions and the corresponding discussions/answers. I have also provided a .html for those who want to view the notebook without launching jupyter.

### Project 3

   3. For this project the primary task was conducting an A/B test on data provided by Udacity. The notebook has much of questions/answer and how each task was performed in python. In a nutshell, I was given data from fictitious company that wants to know whether to launch their new e-commerce website and it was my job to make the recommendation whether they should or should not launch their site. I answered this question using both an A/B test and logistic regression.

### Project 4

   4. For this project my job was to (1) clean Twitter data that was associated with 5,000+ tweets from the WeRateDogs Twitter webpage (this data was provided for me, although I had to import the dataset programatically from the Udacity website) and (2) the data that was given to me did not have "retweet count" and "favorite count" so my job was to obtain this data by querying the Twitter API myself. In addition to querying this data, I also needed to clean it. and lastly (3) present a brief analysis of the data that a Udacity team-member created by classifying each of the dogs using a pre-trained neural network. I discovered a few inconsistencies - one that is noteworthy is that of the dogs were classified as food (remember this is a pre-trained neural network that was trained on images of dogs as well a process known as transfer learning).

      * The report for wrangling the data in (1), (2), and (3) can be found in *wrangle_report.pdf*.
      * The analysis for (3) can be found in *act_report.pdf*.

### Project 5

   5. This project consisted of two parts:

      * Use Python visualization libraries to systematically explore a dataset starting from plots of single variables and building up plots of multiple variables. This is the exploratory data analysis (EDA) phase of the project.

      * Produce a presentation that illustrates interesting properties/findings/trends/relationships that I discovered in the dataset.
##### Data Used for Project 5

NOTE: the data that I used for this project was the same dataset that I used in my project for my *Applied Multivariate Statistical Analysis* class, that is, it's the 1992 election data combined with the webscraped data from Wikipedia using R.

## Important Files (by directory)

### project_1
   * The jupyter notebook used to conduct the analysis is entitled *project_1.ipynb*.
   * The dataset for the global temperature trend is called *results-7.csv*.
   * The dataset for the Atlanta temperature trend is called *results-8.csv*.
   * The SQL queries I used to gather the data is called *sql_queries.sql*.
   * The final report is called *daNdProject1.pdf*.

### project_2
   * The data that I used to conduct my analysis is called *data.csv*.
   * The jupyter notebook that  I used to conduct the analysis is called *project_2_notebook.ipynb*.
   * The .html for convenient viewing is called *project_2_notebook.html*

### project_3
   * The two datasets used for this project are called *ab_data.csv* and *countries.csv*
   * The jupyter notebook used to perform the analysis is called *Analyze_ab_test_results_notebook.ipynb*
   *The .html for convenient viewing is called *Analyze_ab_test_results_notebook.ipynb*.

### project_4
   * The jupyter notebook used for wrangling/analysis is called *wrangle_act.ipynb*.
   * The .html for convenient viewing of the notebook is called *wrangle_act.html*.
   * The archive from Twitter that was given to me is called *twitter-archived-enhanced.csv*.
   * The dataset that contained the dog classifications given to me from Udacity is called *image_predictions.tsv*.
   * The combined dataset that consists of *twitter-archived-enhanced.csv* and the data that I queried from Twitter myself is called *tweet_json.txt*. This dataset was combined using an inner join on tweet id.
   * The report I created for data-cleaning tasks is called *wrangle_report.pdf*
   * The report I created for analyzing the dog classification data is called *act_report.pdf*

### project_5
   * The final presentation/powerpoint is called *final_presentation_jaredthacker.pdf*.
   * The dataset used for this project is called *full_dataset.csv*.
   * The jupyter notebook used to create the exploratory visualizations is called *exploratory_analysis.ipynb*.
   * The jupyter notebook used to create the explanatory visualizations is called *explanatory_visualizations.ipynb*.
   * Likewise the .htmls for convenient viewing is are called *exploratory_visualizations.html* and *explanatory_visualizations.html*.

## Usage
This section is really irrelevant for this repository. All of the projects were completed using jupyter notebooks, so just open those the usal ways to edit/use them.

## License (MIT)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
