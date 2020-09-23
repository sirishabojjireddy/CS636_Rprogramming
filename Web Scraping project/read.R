colns=c("Title", "DOI", "Authors", "Date", "Abstract", "Keywords", "Text")

data<-read.table('MobileDNA.txt',sep = '\t',col.names = colns )

View(data)