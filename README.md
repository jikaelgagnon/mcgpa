# mcgpa
## :trophy: Best Newbie Hack at [MAIS Hacks 2023](https://maishacks2023.devpost.com/)
### What our model predicts
Our model takes as input a list of the user's current courses and professors, alongside their GPA and completed credits and predicts their GPA by the end of the semester. The model takes historical course data and the difficulty of each professor. Furthermore, our model is specific towards McGill students by only training on McGill data, meaning our predictions follow the trends of McGill courses and McGill professors.

### Our dataset
| course | term    | avg   | alltime_avg | prof     |
|--------|---------|-------|-------------|----------|
| ACCT351 | F2016 | 3.0         | 2.991667 | Tsang, Desmond         |
| ACCT351 | F2016 | 3.0         | 2.991667 | Abrams, Amanda         |
| ACCT351 | F2016 | 3.0         | 2.991667 | Marianer, Michael      |
| ACCT351 | F2016 | 3.0         | 2.991667 | Murray, Michael George |
| ACCT351 | W2017 | 3.0         | 2.991667 | Abrams, Amanda         |


To get historical course data, we used [crowdsourced data from McGill Enhanced](https://docs.google.com/spreadsheets/d/1NGUBQuF8FI6ebna86S1RHpc27srxpMbaSyjipIkr-gk/edit#gid=233834959). This dataset contained the majority of our required data, except that it was missing a professor column. We created a web scraper using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to retrieve professor names for every instance. In addition, we added an all-time average column that has the all-time course average.

### How the model works
![image](https://github.com/jikaelgagnon/mcgpa/assets/82888595/5b5b7c47-d221-476b-8397-207817f6f065)

Our model follows an Exponential Moving Average (EMA) model that uses historical class average data in order to predict the next class average in conjunction with prof difficulty. This will place a higher importance on recent data to predict the next class average.

$Average_t = \alpha*ClassAverage_{t-1} + (1-\alpha)Average_{t-1} + Prof$

Where the Prof value is the associated difficulty of the prof with a coefficient of 1, found through linear regression between the class average and professor difficulty in R.

$Prof = \sum \bar X{prof,i} -\bar X_{overall, i}$

Thus, we can use the $Average_t$ equation to find the next predicted class average and put this into the GPA equation.

$GPAt = \frac{TotalCredits_{t-1}GPA_{t-1} + \sum credits_i * Average_{t,i}}{TotalCredits_{t-1} + \sum credits_i}$

### Postscript on R
![image](https://github.com/jikaelgagnon/mcgpa/assets/82888595/8bec5284-3c98-4573-a2fe-06e2fc04b140)
![image](https://github.com/jikaelgagnon/mcgpa/assets/82888595/42c78fc4-1126-411c-82b5-9d664aa4b43e)


Our model found, through simple linear regression in R, that there is a one to one increase between the professor score and the overall course average.
