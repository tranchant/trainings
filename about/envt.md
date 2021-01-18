# Environment

## Appliance NGSanalysisJupyter: Biosphere BASE environment for NGS analysis using Jupyter

The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

This IFB cloud appliance provides both the Jupyter Notebook and Lab environment (see [explanations](https://jupyter.org/index.html)). Biosphere's users can switch these environments simply by changing the relative URL of the service from '/tree' to '/lab'.

This Jupyter app is based on the Jupyter Docker Stacks (see [details](https://jupyter-docker-stacks.readthedocs.io)). By default, this Biosphere app uses the stack `jupyter/datascience-notebook` but users can choose any other existing stack with an Advanced deployment in Biosphere portal.

Main jupyter stacks are:
- `jupyter/minimal-notebook`: Minimally-functional Jupyter Notebook server, Miniconda Python 3.x, Pandoc and TeX Live for notebook document conversion
- `jupyter/r-notebook`: Everything in jupyter/minimal-notebook and popular packages from the R ecosystem.
- `jupyter/scipy-notebook`: Everything in jupyter/minimal-notebook and popular packages from the scientific Python ecosystem.
- `jupyter/datascience-notebook`: Everything in the jupyter/scipy-notebook and jupyter/r-notebook images, plus libraries for data analysis from the Julia, Python, and R communities.
- `jupyter/tensorflow-notebook`: Everything in jupyter/scipy-notebook and popular Python deep learning libraries.

*See a detailed list of available Jupyter stacks [there](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html).*


## Linux : ubuntu 20.04

## Bioinformatics tool 


## Tools

* [Jupyter notebook/lab](https://jupyter.org)
* [fastq-stats](https://expressionanalysis.github.io/ea-utils/)
* [seqtk](https://github.com/lh3/seqtk)
* [NanoPlot](https://github.com/wdecoster/NanoPlot)
* [BWA](https://github.com/lh3/bwa)
* [SAMtools](http://www.htslib.org/)
* [GATK - including Picard-tools](https://gatk.broadinstitute.org/hc/en-us)
* [VCFtools](https://vcftools.github.io/man_latest.html)
* [Minimap2](https://github.com/lh3/minimap2)
* [Sniffles](https://github.com/fritzsedlazeck/Sniffles)
* [SURVIVOR](https://github.com/fritzsedlazeck/SURVIVOR/)
* [sNMF](http://membres-timc.imag.fr/Olivier.Francois/snmf/index.htm)
* [Abyss](https://github.com/bcgsc/abyss)
* [Raven](https://github.com/lbcb-sci/raven)
* [vm](https://biosphere.france-bioinformatique.fr)

## Contact

* [Support Cloud IFB](mailto:biosphere-support@genouest.org) 


## Licence

Licensed under GPLv3
