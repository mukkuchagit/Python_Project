#Annotation of RNA sequencing data using BLAST  (AR-SUB) through Python

##Introduction
It is very useful to know about the presence and level of gene expression in any biological sample at certain time. Modern technique, RNA sequencing (RNA-seq), has enabled us to achieve this task quite well. Through RNA-seq it has been easier to look at cells entire transcriptome. It has also enabled us to study about alternative gene spliced transcripts, post-transcriptional modifications, gene fusion, mutations/SNPs and changes in gene expression [(wikipedia link)](https://en.wikipedia.org/wiki/RNA-Seq ). Another very important field where RNA-seq is used intensively is gene annotation or de-novo predictions [(Zhen et. al. 2011)](http://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-12-540).
After transcriptome assembly with the help of NCBI’s BLAST (Basic Local Alignment Search Tool) the newly sequenced transcripts are annotated (Figure 1). Genes that match to the closely related model organism is considered as homologous and that do not match with any organisms in database are classified as de-novo genes specific to the organism [(any ref…)].


![figure 1](images/project_overview.jpg)


##What does AR-SUB do :question:
AR-SUB will align the assembled transcriptome fragments to the already annotated sequences available in NCBI database of various organisms. Usually, the gene annotation is done by running blast one at a time manually or doing it in Microsoft excel, which is also manual. So, it is hugely time consuming and error prone as well (as we do it manually). with AR-SUB, it will be just three easy steps to get annotation of all the sequenced transcriptome of any organism (Figure 2).

![figure 2](images/Workflow.jpg)


##Requirements and limitations
As AR-SUB was created in Linux operating system and high performance computing (HPC) system, to run this script there are some prerequisites. 

1.	Python version 3 or later are needed to run the program
2.	Most of the scripts use subprocess module so Linux OS is required 
3.	As we are aligning to all the nucleotide database in NCBI, we need BLASTn installed (either in the personal computer hard disc or in the super computer). 
4.	To make it perform faster HPC system is favored more.
5.	The program currently only accepts .*fasta* files as input to so BLAST and gives gene annotations in text (.txt) format.
6.	You need to run the program three times to get annotated genes from three stages (as shown in figure 2). 

Nevertheless, all these requirements are for the best performance so once they are met it is easy to get the output. Furthermore, as the input transcriptome assembly file is generally huge, the time consumed by the program to run will also be accordingly higher.


##How to get started  :+1:

1.	First, create a folder designated only to work for the gene annotation in your computer or supercomputer (HPC). Start with copying your assembled transcriptome *fasta* file in to this folder.
2.	Download and move all files and scripts from the AR-SUB repository on GitHub into the folder you created in step 1. It is necessary to **keep all these files in the same folder** to run the program effectively!
3.	Download the file(s) of Refseq data of the organism(s) that you want to BLAST to (subject data). These will be used to create database files for BLAST.
4.	Now, you are ready for the first BLAST (as in step 1 in figure 2)! In python interactive mode run the *ar-sub_python.py* file; this takes user inputs for the names of files in this order with a space in between:
    * a. Name of the file to create database (*Drosophila* refseq in step 1 in figure 2)
    * b. Name of input *fasta* file (query)
    * c. Name of the file which you want to create for BLAST hits
    * d. Name of the file which you want to create for BLAST non-hits


5.	Relaunch the AR-SUB as in step 4 with following changes only in user inputs (as in step 2 in figure 2):

      a.	Name of the file to create database ( All insect refseq in step 1 in figure 2)
      b.	Name of input *fasta* file (hit file from first BLAST run)
      c.	Name of the file which you want to create for BLAST hits (will be input *fasta*     file for third BLAST)
     d.	Name of the file which you want to create for BLAST non-hits
 

##References 
1.	[https://en.wikipedia.org/wiki/RNA-Seq](https://en.wikipedia.org/wiki/RNA-Seq)

2.	[Zhen L,  Zhonghua Z, Pengcheng Y, Sanwen H, Zhangjun F, Kui L  (2011) RNA-Seq improves annotation of protein-coding genes in the cucumber genome. BMC Genomics, 12:540.](http://bmcgenomics.biomedcentral.com/articles/10.1186/1471-2164-12-540)
