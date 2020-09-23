library(rvest)
library(tidyverse)
library(stringr)

files <- list.files(path="/Users/SirishaBojjireddy/Documents/courses/R programming/articles", pattern="*.html", full.names=TRUE, recursive=FALSE)

for(i in 1:length(files))
  {
  title<-files[i]%>%read_html()%>%html_nodes(".ArticleTitle")%>%html_text()
  title<-str_replace_all(title[i],"[\r\n]","")
  if(length(title)==0)
    {
    title<-'NA'
    }
  else if(length(title)>1)
    {
    title<-paste(title,collapse = ",")
    }
  DOI_b<-files[i]%>%read_html()%>%html_nodes(".ArticleDOI a")%>%html_text()
  DOI_b<-sub("https://doi.org/","",DOI_b)
  DOI_b <- str_replace_all(DOI_b,"[\r\n]","")
  if(length(DOI_b)==0)
  {
    DOI_b<-'NA'
  }
  else if(length(DOI_b)>1)
  {
    DOI_b<-paste(DOI_b,collapse = ",")
  }
  authors<-files[i]%>%read_html()%>%html_nodes(".AuthorName")%>%html_text()
  authors<-str_replace_all(authors,"[\r\n]","")
  if(length(authors)>1)
  {
    authors<-paste(authors,collapse = ",")
  }
  else if(length(authors)==0)
  {
    authors <-'NA'
  }
  # author_affiliations<-files[i]%>%read_html()%>%html_nodes(".aff")%>%html_text()
  # author_affiliations<-str_replace_all(author_affiliations,"[\r\n]","")
  # if(length(author_affiliations)>1){
  #   author_affiliations<-paste(author_affiliations,collapse = ",")
  # }
  # else if(length(author_affiliations==0)){
  #   author_affiliations<-'NA'
  # }
  # m<-files[i]%>%read_html()%>%html_nodes('.al-author-name-more')%>%html_text()
  # m<-str_replace_all(m,"[\r\n]","")
  # m<-grep("Email",m)
  # corresponding_authors<-files[i]%>%read_html()%>%html_nodes('.linked-name')%>%html_text()
  # corresponding_authors<-corresponding_authors[m]
  # corresponding_authors<-str_replace_all(corresponding_authors,"[\r\n]","")
  # if(length(corresponding_authors)>1){
  #   corresponding_authors<-paste(corresponding_authors,collapse=",")
  # }
  # else if(length(corresponding_authors)==0){
  #   corresponding_authors<-'NA'
  # }
  # corresponding_email<-files[i]%>%read_html()%>%html_nodes(".info-author-correspondence a")%>%html_text()
  # corresponding_email<-str_replace_all(corresponding_email,"[\r\n]","")
  # if(length(corresponding_email)>1){
  #   corresponding_email<-paste(corresponding_email,collapse=",")
  # }
  # else if(length(corresponding_email)==0){
  #   corresponding_email<-'NA'
  # }
  publication_date<-files[i]%>%read_html()%>%html_nodes("datePublished")%>%html_text()
  publication_date<-str_replace_all(publication_date,"[\r\n]","")
  if(length(publication_date)==0){
    publication_date<-'NA'
  }
  else if(length(publication_date)>1){
    publication_date<-paste(publication_date,collapse = ",")
  }
  abstract<-files[i]%>%read_html()%>%html_nodes(".Abstract")%>%html_text()
  if(length(abstract)==0){
    abstract<-'NA'
  }
  else if(length(abstract)>1){
    abstract<-paste(abstract,collapse = ",")
  }
  key_words<-files[i]%>%read_html()%>%html_nodes("#Keywords")%>%html_text()
  key_words<-str_replace_all(key_words,"[\r\n]","")
  if(length(key_words)>1){
    key_words<-paste(key_words,collapse = ",")
  }
  else if(length(key_words)==0){
    key_words<-'NA'
  }
  full_text<-files[i]%>%read_html()%>%html_nodes("#main-content")%>%html_text()
  full_text<-str_replace_all(full_text,"[\r\n]","")
  full_text<-str_replace_all(full_text," ","")
  if(length(full_text)==0){
    full_text<-'NA'
  }
  else if(length(full_text)>1){
    full_text<-paste(full_text,collapse = ",")
  }
  information=c(title,DOI_b,authors,publication_date,abstract,key_words,full_text)
  #information=c(title,DOI_b,authors,author_affiliations,corresponding_email,corresponding_authors,publication_date,abstract,key_words,full_text)
  required_output <- matrix(information,1,7)
  
  write.table(required_output, "MobileDNA.txt", row.names = FALSE, col.names = FALSE, sep = "\t", append = TRUE)
  
}