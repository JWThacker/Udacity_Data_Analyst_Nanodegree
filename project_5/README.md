I decided to use a dataset that I compiled using demographic dataset from ufl.edu and webscraped data from Wikipedia. Details can be found in the report and powerpoint.

The dataset has 11 variables of interest that will be used in this dataset. The variables are described below.

   The dataset has 9 predictor variables:
      * Median Age - the median of individuals in the county  
      * Mean Savings - the mean savings an individual has in USD ($)
      * Per Capita Income - The average income made per person in a county
      * Percent in Poverty - The percentage of a county that lives below the poverty line.
      * Percent Veterans - The percentage of people that have served in a branch of the armed forces.
      * Percent Female - The percentage of individuals in the county that are female.
      * Population Density - The population per square unit (unspecified in the original dataset, my guess is # of people / square mile) in each county.
      * Percent In Nursing Homes - The percentage of people that live in a nursing home in each coutny.
      * Crime Index (Per Capita) - the crime index per unit of the population (unspecified in the original dataset, my guess is per 100,000 people).
    The dataset has 1 response variable:
      * Clinton Win - Whether Clinton won or lost the election in a given coutny. The value is True if Clinton won the election and False otherwise.
    The dataset has 1 variable that is not used in prediction or analysi, but is nice to have to look at outliers and also to have a geographical location to look at for analysis.

Main findings (Exploratory Analysis):
   * Most of the variables did not adhere to the normal distribution, however, once transformed all but one responded well and seemed to adhere to normality.
      * The one variable that did not respond well to transformations we the 'percent_female' variable. This variable appears to have a mostly symmetric distribution but with a faint
        long left tail. Since the distribution seems to be symmetric about the mean, with the exception of the tail, it should be not be a problem if I need to use a data model that 
        requires normality. 
   * The assumptions of MANOVA hold. There is only one more to check, within sample independence, but that will be check after fitting and the using the MANOVA to find the residuals.
      * In addition, the sample size is large enough such that we can relax the normality assumption and homogeneity of covariance assumption.
   * Class imbalance does not exist in the response variable of this dataset, each class is approximately equally represented.
   * We can visually see why the null hypothesis is rejected in the MANOVA by looking at the boxplots in the report and powerpoint.
   * Correlation does exists between some of the predictors in the dataset, therefore, this dataset will likely benefit from a PCA.
   * When performing the full PCA, four components should be retained.

Main findings (Explanatory Analysis):
   * The response levels are equally balanced.
   * States that were won by a partisan candidate were won with a vote percentage of less than 50% the vast majority of the time. This indicates a strong independent candidate
     presence among voters for the year of 1992. 
   * The southeast had a suprisingly large percentage of voters that voted for a left-leaning candidate - normally the southeast is a republican stronghold.
   * Bill Clinton won the 1992 election in a landslide - all regions of the U.S had their majority of voters side with Clinton.


Aside, from the Python documention and a few websites like GeeksForGeeks to see how certain fucntions can be used, all the code is my own. I don't plagiarize code, that makes it no fun for me.
