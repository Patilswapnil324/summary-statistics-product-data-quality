# summary-statistics-product-data-quality
script for creating  a statistical summary  for administrative data  .i.e(village,district,city &amp; grid  level)
script for checking summary statistics of product data this script include code for checking statistical summary of administrative files.i.e(district,city,village & ho8) & creating a new file as well as appending all the data into a single file for product development analysis.

things need to keep in mind before running this script- 1.in the 2nd block of sript need to assign some parameters which are diffrent for each file as mentined above.following are the parameters path,Unique_column,Level,Table_name,remove so assigning this parameters whith proper data columns is manadtory for getting exact results.

for each file(i.e district,city,village & ho8) script need to be run every time). when the script is running first time then second last block need to be run to save the file first time & last block code should be disable. after that every time whenever script is running then second last block should be disable & exceute last block to append the results in exisiting file.
