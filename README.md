# term-extraction-nlp
Natural Language Processing Final Project: German version of The Termolator (terminology extraction system)

The Termolator takes two sets of documents as input a FOREGROUND set and a BACKGROUND set and finds instances of terminology that are more characteristic of the FOREGROUND than the BACKGROUND. 

The essential details of the June 2018 system are described in the following paper:

A. Meyers, Y. He, Z. Glass, J. Ortega, S. Liao,
A. Grieve-Smith, R. Grishman and O. Babko-Malaya (2018).  The
Termolator: Terminology Recognition Based on Chunking,
Statistical and Search-Based Scores Research Metrics and
Analytics (RMA).
This can be downloaded at:

https://www.frontiersin.org/articles/10.3389/frma.2018.00019/full

Instructions for Using our program:

To run the distributional component, you must be in the directory term_extraction_nlp/GERMAN-test:

```term_extraction_nlp/distributional_component.py NormalRank foreground_new.list german_final_output.all_terms False background_new.list```

Output of this can be found at ```term_extraction_nlp/GERMAN-test/german_final_output.all_terms```
