# GTEX
________________________________________________________________________________________________________________________

GTEX-Muscle_Brain.xlsx: https://drive.google.com/file/d/0Bzv1SNKM1p4uRkI3TkZkZE9vZXM/view?usp=sharing
________________________________________________________________________________________________________________________

# General workflow

1. Downloaded 4.9 Gb file from GTEX. With the RPKM RNAseq file.
2. Got a list of IDS from the metadata file from donors with age range 20-29 and 70-79.
3. Used the list of IDs to extract only those IDs from the GTEX file
4.
  A: Filter out all rows that summed 0 
  B: 5% or more 0 values

File: Muscle_tex_CD_upload_to_enrichr: Caracteristic direction results uploaded to enrichr


### Enrich result link 
  http://amp.pharm.mssm.edu/Enrichr/enrich?dataset=3tk2

### L1000CDS2
  Prediction reverse
  http://amp.pharm.mssm.edu/L1000CDS2/#/result/56a68aaf439f8cf80020858c

  Prediction mimic
  http://amp.pharm.mssm.edu/L1000CDS2/#/result/56a68ca5439f8cf8002085b0

________________________________________________________________________________________________________________________

*Scripts:*

**1. get_only.py:** Get specific samples from GTEX. 
  *File A:* samples wanted.
  *File B:* GTEX file (GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_rpkm.txt).
