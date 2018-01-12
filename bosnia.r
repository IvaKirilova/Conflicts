library('tidyverse')
bosnia <- read.csv('Bosnia.csv')
library(maps)
library(mapdata)

bosnia['Best_Estimate'] <- NA
bosnia$Best_Estimate <- as.numeric(as.character(bosnia$best))

croatia <- read.csv('Croatia.csv')

croatia['Best_Estimate'] <- NA
croatia$Best_Estimate <- as.numeric(as.character(croatia$best))

write.csv(bosnia, 'bosnia1')
write.csv(croatia, 'croatia1')

globe <- map_data('world')



ggplot() +
  geom_polygon(data = filter(globe, globe$region == "Bosnia and Herzegovina"), mapping = aes(x = long, y = lat, group = group), fill = NA, colour = 'black') +
  geom_polygon(data = filter(globe, globe$region == "Croatia"), mapping = aes(x = long, y = lat, group = group), fill = NA, colour = 'black') +
  geom_point(data = bosnia, mapping = aes(x = longitude, y = latitude, size = best, colour = year)) +
  geom_point(data = croatia, mapping = aes(x = longitude, y = latitude, size = best, colour = year)) 

ggplot() +
  geom_bar(data = bosnia, mapping = aes(x = year), colour = 'red') +
  geom_bar(data = croatia, mapping = aes(x = year), colour = 'blue')


  

