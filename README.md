# Problem

##Preliminary information
There is a service that returns a list of articles in the form of json
https://jsonmock.hackerrank.com/api/articles?page={page_number}

Where {page_number} is an integer indicating the page whose articles you want to query.

Each query returns information in the form of json:

- **page** - the page number whose data is currently being returned
- **per_page** - number of articles per page
- **total** - the total number of articles on all pages
- **total_pages** - the total number of pages containing articles
- **data** - an array in the form of json of objects that contain information about articles (title, url,
  author, num_comments, story_id, story_title, story_url, parent_id, created_at)

For example, the following query returns a list of the first page:
https://jsonmock.hackerrank.com/api/articles?page=1


##Implement
Write a Python script that finds and returns the titles of the ten articles with the most comments
(num_comments) in descending order of number of comments over all pages. 

The title of the article is the "title" field value in the article information, if there is no "title" field value, then the
"story_title" field value, if both field values are missing than ignore such an article and select the
article with the most comments next.

##How to get help

```make help```

##How to install script

```make install```

##How to run script

```make run number_of_results=15```
- **number_of_results** - number of results to show (Default: 10)

##How to run tests

```make test```

##What to do if you do not have makefile

Just run
```
pip install -r requirements.txt
python top_commented_articles.py -r $(number_of_results)
```
- **number_of_results** - number of results to show (Default: 10)

or 

```
pip install -r requirements.txt
python -m unittest test
```

##Questions and answers

### What python version is used

I used Python 3, but it is easy to rewrite it using Python 2.

### What to do if you want to change amount of returned articles (now it is 10)

I added parameter **number_of_results** for it

### What happened if it will be thousands of pages with millions of articles. 

First of it will depend, how fast it will fetch data from hackerrank page. 
We can use multithreading to get results asynchronously at this case. Most probably, we will
need to think about the fastest algorithm to sort results. 


