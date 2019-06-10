import colabimport
colabimport.get_notebook('https://github.com/ratmcu/colaboratory_import/blob/master/nb_sample.ipynb?raw=true')
# import io, os, sys, types
import nb_sample
pg = nb_sample.PageContents('https://en.wikipedia.org/wiki/Joachim_Gauck')
info_card = nb_sample.InfoCard(pg)
pe = nb_sample.PrivateEntities(info_card)