library(rvest)
library(stringr)

enter<-function(year)
{
  web=paste0('https://mobilednajournal.biomedcentral.com/articles?query=&volume=', 
             
             switch(year, "2019"=10, "2018" =9, "2017"=8, "2016"=7, "2015"=6, "2014"=5, "2013"=4, "2012"=3, "2011"=2, "2010"=1), 
             
             '&searchType=&tab=keyword')
  
  Link<-web%>%read_html()%>%html_nodes(".c-teaser__title a" )%>%html_text()
  L2<-web%>%read_html()%>%html_nodes(".c-teaser__title a" )%>%html_attr("href")
  
  for (i in 1:length(L2))
    {
    L2[i]<-substring(L2[i],11)
    }
  
  for(i in 1:length(L2))
    {
    download.file(paste0('https://mobilednajournal.biomedcentral.com/track/pdf/',L2[i]), destfile="test.pdf", mode='wb')
    }
  
}
enter("2019")