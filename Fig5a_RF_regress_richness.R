
require(randomForest) #
library(reshape2) #
library(vegan) #
library(ggplot2) 
library(splines) #
require(modelr)
library(data.table)

env.meta <- read.csv("AP_environ1372.csv",row.names = 1,as.is = TRUE)

set.seed(1000)
richness.rf<- randomForest(richness ~ mat+map+dp+biomass+ph+clay+cfv+soc+rad+brdf+northness+ref+entropy+evaporation+pd+hdi, data=env.meta,na.action = na.omit,importance = TRUE, RMSE=TRUE, ntree = 1200, nrep = 1000,mtry=10, nodesize=1, num.cores = 8)



mat <- fread("mat.csv")
map <- fread("map.csv")
dp <- fread("dp.csv")
ph <- fread("ph.csv")
clay <- fread("clay.csv")
cfv <- fread("cfv.csv")
soc<- fread("soc.csv")
rad<- fread("rad.csv")
brdf<- fread("brdf.csv")
ref<- fread("ref.csv")
biomass<- fread("biomass.csv")
northness<- fread("northness.csv")
entropy<- fread("entropy.csv")
evaporation<- fread("evaporation.csv")
hdi<- fread("hdi.csv")
pd<- fread("pd.csv")


mat <- data.frame(mat)
map <- data.frame(map)
dp <- data.frame(dp)
ph <- data.frame(ph)
clay <- data.frame(clay)
cfv <- data.frame(cfv)
soc<- data.frame(soc)
rad<- data.frame(rad)
brdf<- data.frame(brdf)
ref<- data.frame(ref)
biomass<- data.frame(biomass)
northness<- data.frame(northness)
entropy<- data.frame(entropy)
evaporation<- data.frame(evaporation)
hdi<- data.frame(hdi)
pd<- data.frame(pd)

a <- matrix(nrow=18000,ncol=36000)

for (i in 1:36000){
env.meta <- data.frame(mat=mat[,i],map=map[,i],dp=dp[,i],ph=ph[,i],clay=clay[,i],cfv=cfv[,i],soc=soc[,i],rad=rad[,i],brdf=brdf[,i],ref=ref[,i],biomass=biomass[,i],northness=northness[,i],entropy=entropy[,i],evaporation=evaporation[,i],pd=pd[,i],hdi=hdi[,i])

colnames(env.meta)<-c("mat","map","dp","ph","clay","cfv","soc","rad","brdf","ref","biomass","northness","entropy","evaporation","pd","hdi")
A1.pred <- predict(richness.rf, newdata=env.meta, type = "response")
a[,i] <- A1.pred
}

fwrite(a,"AP_regress_richness2023.csv",col.names=F,sep=",")

