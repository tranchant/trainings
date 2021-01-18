# Training introduction

This book contains information about the planet **Jupiter** - the fifth planet from the sun and the largest planet in the solar system!


```{figure} image.png
---
height: 150px
name: my-image
---
Here is my image's caption!
```

```{figure} https://solarsystem.nasa.gov/system/resources/detail_files/2486_stsci-h-p1936a_1800.jpg
---
height: 300px
name: jupiter-figure
---
The beautiful planet Jupiter!

Jupiter has a mass of:  $m_{j} \approx 1.9 \times 10^{27} kg$

$$
  m_{j} \approx 1.9 \times 10^{27} kg
$$

```{math}
:label: my_label
m_{j} \approx 1.9 \times 10^{27} kg
```

## Environment

* Linux 
* Bioinformatics tool 
* https://biosphere.france-bioinformatique.f
* slack :

## Program 

# Monday "Discovering the linux world throught jupyter world"


1h30 -> pause

Présentation formations / formateurs

Préambule : lancement machine virtuelle -> garder vm allumée

attentes participants

Présentation/cours ~45 min

Méthodo de séquençage rapide

cas d'applications

1h15 post - pause

Lancement jupyter book bash ~ 1heure

commencer avec linux : ls cd pwd cat wc -l grep pipe

introduire exemple exo applicatifs

Après midi

Linux

exercices compter nb reads / fastq stat

plot jupyter stat ?

quelles analyses ? gff - bedtools intersect localisation capture

Exercice qui tue/Bonus !!!! pipe

Jour2

1h30 -> pause

30-45 minutes : debrief veille

Présentation Mapping ? format rapide ? - 30 minutes ? sam . flagstat (page liens outils url) - appel SNP (format vcf)

PAUSE

Jupyter book bash

mapping un individu GATK4 * bwa aln/sampe / picardtools / appel SNP

explciation TP Pipeline à faire pour les 15 individus (boucle / 1 par 1)

Gestionnaire WF Nextflow WF CRG ? presentation 10 min -> TOGGLE

Après midi

TP Pipeline (canveas : boucle, TOGGLe)

15 vcfs, puis 1 vcf final

Jour3

1h30 -> pause

30-45 minutes : debrief veille

Visualisation bam indiv 13/14 TABLET

PAUSE

Jupyter book bash

SNP filtering

ACP code R ?

snmf

Après midi

Canveas : ACP code R

plot variant snp (densité filtré / non filtré)

Jour4

1h30 -> pause

30-45 minutes : debrief veille

Presentation Longread methodo + applications SV

PAUSE

Jupyter book bash

nanoplot

mapping reads ONT vs Genome ref avec minimap2 et un individu

Après midi

Sniffle (documentation par eux meme)

vcf sniffle / vcf SNP

plotter carte densité SNP / SV

Jour5

1h30 -> pause

30-45 minutes : debrief veille

principe Assemblage Short read / Longread Nucmer

pause

assemblage short read (abyss) / long read (raven)

Dgenies

Applications : synthese techno short et long reads (pdf)

Après midi

15 assembkages et comparaison (short/long read) -> essayer comprendre ce qui s ets passé pour l organisme

synthèse 16h ?

We can estimate the mass of Jupiter from the period and size of an object orbiting it. For example, we can use Jupiter's moon Callisto to estimate it's mass.

Callisto's period: $p_{c}=16.7 days$

Callisto's orbit radius: $r_{c}=1,900,000 km$

Now, using [Kepler's Law](https://solarsystem.nasa.gov/resources/310/orbits-and-keplers-laws/) we can work out the mass of Jupiter.

```{math}
:label: eq1
m_{j} \approx \frac{r_{c}}{p_{c}} \times 7.9 \times 10^{10}
```

```{math}
:label: eq2
m_{j} \approx 1.9 \times 10^{27} kg
```


```{margin} Did you know?
Jupiter is 11.0x larger than Earth!
```

## Linux

```{note}
I am a useful note!
```

```{tip}
I am a useful note!
```

```{warning}
I am a useful note!
```

```{hint}
NASA provides a lot more information about the physical characteristics of Jupiter [here](https://solarsystem.nasa.gov/planets/jupiter/by-the-numbers/).
```


There might even be more planets out there with a similar mass to Jupiter {cite}`mayor1995jupiter`!

## Bibliography

```{bibliography} references.bib
```
 DAY 1 


###### Discover the NGS world !  __link__

```{figure}  https://lh3.googleusercontent.com/proxy/1rPwglBhZPOjyZDv_HOvsDuZBBlHTXOj064R8O06vycCmluJzzlkSoEfiD2KPZBDuKeKQYk2XBnA02BrG0mKuqOe1qeyfaMgihpNTwk
---
height: 100px
name: imgCof
---
```

###### Discovering the linux world throught jupyter world

* ls cd pwd cat wc -l grep pipe
* introduire exemple exo applicatifs


```{figure} https://www.potentialplusuk.org/wp-content/uploads/2020/07/Homework.jpeg
---
height: 100px
name: imgHW
---
```


* exercices compter nb reads / fastq stat

* plot jupyter stat ?

* quelles analyses ? gff - bedtools intersect localisation capture

* Exercice qui tue/Bonus !!!! pipe

------------------------------------------------------------


# DAY 2

###### Discover the mapping and SNP calling methodology

```{figure}  https://lh3.googleusercontent.com/proxy/1rPwglBhZPOjyZDv_HOvsDuZBBlHTXOj064R8O06vycCmluJzzlkSoEfiD2KPZBDuKeKQYk2XBnA02BrG0mKuqOe1qeyfaMgihpNTwk
---
height: 100px
name: imgCof
---
```

###### Mapping & SNP calling on one sample
mapping un individu GATK4 * bwa aln/sampe / picardtools / appel SNP

###### Mapping and SNP calling on several samples
à faire pour les 15 individus (boucle / 1 par 1)

## Gestionnaire WF Nextflow WF CRG ? presentation 10 min -> TOGGLE

```{figure} https://www.potentialplusuk.org/wp-content/uploads/2020/07/Homework.jpeg
---
height: 100px
name: imgHW
---
```

* TP Pipeline (canveas : boucle, TOGGLe)

* 15 vcfs, puis 1 vcf final

------------------------------------------------------------

# DAY 3 

* Visualisation bam indiv 13/14 TABLET

* SNP filtering

* snmf

```{figure} https://www.potentialplusuk.org/wp-content/uploads/2020/07/Homework.jpeg
---
height: 100px
name: imgHW
---
```

* Canveas : ACP code R

* plot variant snp (densité filtré / non filtré)

------------------------------------------------------------


#  DAY 4

* Presentation Longread methodo + applications SV

```{figure}  https://lh3.googleusercontent.com/proxy/1rPwglBhZPOjyZDv_HOvsDuZBBlHTXOj064R8O06vycCmluJzzlkSoEfiD2KPZBDuKeKQYk2XBnA02BrG0mKuqOe1qeyfaMgihpNTwk
---
height: 100px
name: imgCof
---
```

* nanoplot
* mapping reads ONT vs Genome ref avec minimap2 et un individu

```{figure} https://www.potentialplusuk.org/wp-content/uploads/2020/07/Homework.jpeg
---
height: 100px
name: imgHW
---
``` 

* Sniffle (documentation par eux meme)

* vcf sniffle / vcf SNP

* plotter carte densité SNP / SV

------------------------------------------------------------


# DAY 5

* principe Assemblage Short read / Longread Nucmer

pause

* assemblage short read (abyss) / long read (raven)

* Dgenies

* Applications : synthese techno short et long reads (pdf)

```{figure} https://www.potentialplusuk.org/wp-content/uploads/2020/07/Homework.jpeg
---
height: 100px
name: imgHW
---
``` 

* 15 assembkages et comparaison (short/long read) -> essayer comprendre ce qui s ets passé pour l organisme

* synthèse 16h ?


------------------------------------------------------------

# Contributing

# Creators

# Thank

# Copyright and license 


## Linux

```{note}
I am a useful note!
```

```{tip}
I am a useful note!
```

```{warning}
I am a useful note!
```

```{hint}
NASA provides a lot more information about the physical characteristics of Jupiter [here](https://solarsystem.nasa.gov/planets/jupiter/by-the-numbers/).
```


There might even be more planets out there with a similar mass to Jupiter {cite}`mayor1995jupiter`!

## Bibliography

```{bibliography} references.bib
```