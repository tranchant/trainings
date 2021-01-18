# Day 2

###### Openning session



###### Discovering the mapping

* [Slides](url)
* jupyter book:
* Gestionnaire
* jupyter TP






30-45 minutes : debrief veille

Présentation Mapping ? format rapide ? - 30 minutes ? sam . flagstat (page liens outils url) - appel SNP (format vcf)

PAUSE

Jupyter book bash

mapping un individu GATK4 - bwa aln/sampe / flagstat / picardtools / appel SNP

NB parler des @RG mais ne pas montrer la commande

Gestionnaire WF Nextflow : https://nf-co.re/ 10 minutes

explication TP Pipeline à faire pour les 15 individus (boucle / 1 par 1)

Dans meme cellule pour un individu : 4 commandes plus creation arborescence mkdir Mapping / SNP

introduction for avec ls :

for i in {1..15}; do mkdir Clone$iDir; mkdir Clone$iDir/mapping; mkdir Clone$iDir/snp ; mv Clone$i_* Clone$iDir/.; done

for i in ls; do echo $i; ls $i; done