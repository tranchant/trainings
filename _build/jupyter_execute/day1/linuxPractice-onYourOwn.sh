PUT YOUR COMMAND HERE

PUT YOUR COMMAND HERE

PUT YOUR COMMAND HERE

PUT YOUR COMMAND

ls /ifb/data/mydatalocal/LINUX-TP/Bank

ls /ifb/data/mydatalocal/LINUX-TP/Bank/*fasta

PUT YOUR COMMAND

PUT YOUR COMMAND

PUT YOUR COMMAND

PUT YOUR COMMAND

PUT YOUR COMMAND

fastq-stats -D  /ifb/data/mydatalocal/fastqDirLR/Clone9-LR.fastq 

fastq-stats -D  /ifb/data/mydatalocal/fastqDirLR/Clone9-LR.fastq  > /ifb/data/mydatalocal/fastqDirLR/Clone9-LR.fastq-stats

ls /ifb/data/mydatalocal/fastqDirLR/*fastq

ls /ifb/data/mydatalocal/fastqDirLR/*fastq-stats

cat /ifb/data/mydatalocal/fastqDirLR/Clone9-LR.fastq-stats

cd /ifb/data/mydatalocal/fastqDirLR/
pwd

for file in *; do 
    echo " $file";
done;

for file in *fastq; do 
    echo " File read : $file";
done;

for file in *fastq; do 
    echo "File read : $file ";
    echo -e "File to create : $file-stat \n";
done;

# PUT YOUR COMMAND WITH fastq-stats + redirection in a for loop


python3 /ifb/data/mydatalocal/LINUX-TP/Script/parseFastqStat.py -dir ifb/data/mydatalocal/fastqDirLR/ -f /ifb/data/mydatalocal/fastqDirLR.statsMerged.csv

PUT YOUR COMMAND

PUT YOUR WGET COMMAND

head -n 20 all.chrs.con

tail -n 20 all.chrs.con

wc -l all.chrs.con

grep ">" all.chrs.con

grep ">" all.chrs.con -c

grep "exon" all.gff3 | head

grep "exon" all.gff3 -c

cat qtl.bed

PUT YOUR COMMAND with -fi and -bed options

PUT YOUR COMMAND with -fi and -bedand -fo options

fastaFromBed -fi all.chrs.con -bed qtl.bed -fo qtl.bed.fasta
bedtools intersect -a all_gene.gff3 -b qtl.bed

PUT YOUR COMMAND 
