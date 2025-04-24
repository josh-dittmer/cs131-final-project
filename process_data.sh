rm -f data/winequality-combined.csv
rm -f data/winequality-processed.csv

# combine the two datasets
head -n 1 data/winequality-red.csv > data/winequality-combined.csv
tail -n +2 data/winequality-red.csv >> data/winequality-combined.csv
tail -n +2 data/winequality-white.csv >> data/winequality-combined.csv

# remove duplicates
(head -n 1 data/winequality-combined.csv && tail -n +2 data/winequality-combined.csv | sort | uniq) >| data/winequality-processed.csv

rm data/winequality-combined.csv