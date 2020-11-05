We developed 3 R scripts for crawling, parsing and reading the articles from html pages mentioned below respectively

Crawler.R

1) We created a function with year as parameter.
2) We used a paste command to take the 
3) switch for the year
4) Create a folder to download all the html files
5) Loop for the html in articles folder and download each file

parser.R

1) Split the data and analyze according to the attributes required by us\

read.R

1) Read the following attributes from the html files downloaded
"Title", "DOI", "Authors", "Date", "Abstract", "Keywords", "Text"
