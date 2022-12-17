install.packages(c("FactoMineR", "factoextra"))
library("FactoMineR")
library("factoextra")
library("corrplot")
library("ggpubr")





setwd("./~")

df<- read.csv("AP_degreetop25_MAC_P.csv", header= T,row.names=1,quote="",check.names = T)##
head(df)
#typeof(df$ABCtransporter)

ARG<-df
ARG.active <- df[1:144, 4:28]

head(ARG.active[, 1:6], 3)

res.mca <- MCA(ARG.active, graph = FALSE)

scree.plot <-fviz_mca_biplot(res.mca, 
                repel = TRUE, # Avoid text overlapping (slow if many point)
                ggtheme = theme_minimal())


var <- get_mca_var(res.mca)
var
var.mca <-fviz_mca_var(res.mca, choice = "mca.cor", 
             repel = TRUE, # Avoid text overlapping (slow)
             ggtheme = theme_minimal())

ggexport(plotlist = list( var.mca), filename = "MCA1.pdf")##

fviz_screeplot(res.mca, addlabels = TRUE, ylim = c(0, 45))



fviz_contrib(res.mca, choice = "var", axes = 1:2, top = 20)



ind <- get_mca_ind(res.mca)
ind
ind.plot<- fviz_mca_ind(res.mca, col.ind = "cos2", 
             gradient.cols = c("#00AFBB", "#E7B800", "#FC4E07"),
             repel = TRUE, # Avoid text overlapping (slow if many points)
             ggtheme = theme_minimal())
ggexport(plotlist = list( ind.plot), filename = "MCA_ind.pdf")##
fviz_cos2(res.mca, choice = "ind", axes = 1:2, top = 30)

##Color individuals by groups,
fviz_mca_ind(res.mca, 
             label = "none", # hide individual labels
             habillage = "multidrug__TolC", # color by groups 
             palette = c("#00AFBB", "#E7B800"),
             addEllipses = TRUE, ellipse.type = "confidence",
             ggtheme = theme_minimal())




res.mca <- MCA(ARG, quali.sup = 1:3,
                 graph=FALSE)##quali.sup = 1
Or

res.mca <- MCA(ARG, quali.sup = 2,
               graph=FALSE)##quali.sup = 1
fviz_mca_biplot(res.mca, repel = TRUE,
                ggtheme = theme_minimal())

fviz_mca_var(res.mca, choice = "mca.cor",####
             repel = TRUE)

ind.mca<-fviz_mca_ind(res.mca, choice = "mca.cor",
             label = "none", # hide individual labels
             habillage = "Phylum", # color by groups 
             palette = c("#006FA6","#A30059","#FFDBE5","#7A4900","#63FFAC","#B79762","#FDE8DC"),
             addEllipses = TRUE, ellipse.type = "confidence",
             repel = TRUE) 

ggexport(plotlist = list( ind.mca), filename = "MCA_ind_mca.pdf")#

fviz_mca_var(res.mca, choice = "mca.cor",
              # hide individual labels
             habillage = "Sick_object", # color by groups 
             palette = c("#006FA6","#A30059","#FFDBE5","#7A4900","#63FFAC","#B79762","#FDE8DC"),
             addEllipses = TRUE, ellipse.type = "confidence",
             repel = TRUE)



res.mca <- MCA(ARG, quali.sup = 1:3,
               graph=FALSE)##quali.sup = 1


biplot.mca <- fviz_mca_biplot(res.mca,
                              habillage = "Sick.object",
                              label = "var",
                              palette = c("#006FA6","#A30059","#FFDBE5","#7A4900","#63FFAC","#00FFFF"),
                              col.var ="black", 
                              col.quali.sup ="dodgerblue4",
                              invisible = "quali.sup",
                              select.var = list(cos2= 10), 
                              shape.ind =15,
                              repel = TRUE,
                              geom.ind = "text", 
                              addEllipses = TRUE, 
                              ellipse.type = "confidence",
                              ellipse.alpha=0.1,  
                              ellipse.level=0.99)#

ggexport(plotlist = list( biplot.mca), filename = "MCA_group.pdf")##


biplot.mca <- fviz_mca_biplot(res.mca,
                              habillage = "Class",
                              label = "var",
                              palette =c("#FF8100","#007B25","#FD0006","#530FAD","#FF90C9","#0AA6D8","#FFB500","#C2FFED","#A079BF"),
                              col.var ="black", 
                              col.quali.sup ="dodgerblue4",
                              invisible = "quali.sup",
                              select.var = list(cos2= 10), ##
                              shape.ind =15,
                              repel = TRUE,
                              geom.ind = "text", 
                              addEllipses = TRUE, 
                              ellipse.type = "confidence",
                              ellipse.alpha=0.1,  ##
                              ellipse.level=0.99)##0

