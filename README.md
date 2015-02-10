# MPCS 50101 Winter 2015 Midterm

### GIVEN:

1. The `midterm.py` code.

2. A file of movie data: `imdb_top250.csv`

   Columns are: IMDB ID,Title,Director,Rating,Year

3. This movie web service:

   `http://www.omdbapi.com/?i={IMDB_MOVIE_ID}&plot=short&r=json`

   Example:
   http://www.omdbapi.com/?i=tt0076759&plot=short&r=json

4. The amazing world of the internet

### THE GOAL:

When you run `midterm.py`, the output should be:

```
* All assertions passed. Nice work!
* Remember to sync your code to GitHub and ensure that it's there!
* Have a nice week!
```

### RULES:

1. Fork and clone this repository before working on it.

1. Any changes to `midterm.py` file will be ignored.  You can modify it
   to aid your debugging (i.e. adding print() statements, etc)
   but your changes will be ignored during grading.

2. Your solution MAY NOT contain any special knowledge of
   any movie data.  You MAY NOT hardcode any movie titles,
   ratings, plot descriptions, identifiers, etc.

3. If you would like to import additional modules:
   - You can only import standard library modules
   - Remember: you can not change THIS file at all

### GRADING RUBRIC:
- [25 pts] 5 points for each passing assertion
- [5  pts] Overall quality (subjective)

Subjective criteria are: readability, naming conventions, efficiency, etc.
