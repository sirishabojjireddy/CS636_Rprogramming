{\rtf1\ansi\ansicpg1252\cocoartf1671\cocoasubrtf400
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Algorithm\
\
We developed 3 R scripts for crawling, parsing and reading the articles from html pages mentioned below respectively\
\
Crawler.R\
1) We created a function \'93enter\'94 with year as parameter.\
2) We used a paste command to take the \
3) switch for the year\
4) Create a folder \'93articles\'94 to download all the html files\
5) Loop for the html in articles folder and download each file\
\
parser.R\
1) Split the data and analyze according to the attributes required by us\
\
read.R\
1) Read the following attributes from the html files downloaded\
"Title", "DOI", "Authors", "Date", "Abstract", "Keywords", "Text"\
\
}