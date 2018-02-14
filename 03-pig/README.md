# Universidad EAFIT
# Curso Big Data - Postobon, 2018-1
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

## Ejecutar programas desde web en PIG:

PIG View:

      lines = LOAD '/user/<<username>>/datasets/gutenberg-txt-es/*.txt' AS (line:chararray);
      words = FOREACH lines GENERATE FLATTEN(TOKENIZE(line)) as word;
      grouped = GROUP words BY word;
      wordcount = FOREACH grouped GENERATE group, COUNT(words);
      DUMP wordcount;
