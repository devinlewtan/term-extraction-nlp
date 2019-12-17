#!/bin/env bash

##args
##$1: wikiurl
##$2: category name
##$3: final output dir name
##$4: article_list
##$5: subcat_list
##$6: recursion option, true or false

wiki_url=$1

##modify category name if contains spaces
rep1="%20"
rep2="_"
catnamewiki=${2// /$rep1}
catnamefile=${2// /$rep2}
final_outfile=$3 ##will already have been created
article_list=$4
subcat_list=$5
recurs=$6

echo
echo "Getting category: $catnamefile"

##Step 1: use php command to get list of categories/pages under desired category

php_qry="/w/api.php?action=query&list=categorymembers&cmtitle=Category:$catnamewiki&cmlimit=max&format=json"

outputfile="${catnamefile}_wiki_apilist"

wget -a "wget_logfile" -O $outputfile $wiki_url$php_qry

##read file in as string
listfile=$(<$outputfile)
listfilecontent=$listfile

##test if this category exists
if [[ ${#listfilecontent} -lt 70 ]]; then
        echo "This category was not found on Wikipedia."
        exit
fi



## ----------- Step 2: extract pageid, ns, title from json format and print to new file

##create new file to write in format: pageid \t ns \t title on each line
outfile="${catnamefile}_categorylist.txt"
if [ ! -e $outfile ]; then
       echo >> $outfile
fi

echo $listfilecontent | python3 -c '
import sys, json
dict=json.load(sys.stdin)
ln=len(dict["query"]["categorymembers"])
for i in range(ln):
        print(dict["query"]["categorymembers"][i]["pageid"], "\t", \
        dict["query"]["categorymembers"][i]["ns"], "\t", \
        dict["query"]["categorymembers"][i]["title"], flush=True)' | tee $outfile


## ----------- Step 3: gather article ids and subcategory ids in files


while IFS= read -r line; do
        #echo "text read from file: $line"
        ns=$( echo "$line" | cut -d $'\t' -f2 )

	if [[ $ns -eq 0 ]]; then
        	id=$( echo "$line" | cut -d $'\t' -f1 )
                #echo "article id: $id"

		if grep -Fxq "$id" $article_list; then
			:
			#echo "article already found. skipping."
		else
			echo "$id" >> $article_list
                fi

	elif [[ $ns -eq 14 ]]; then  ## if ns = 14: subcategory
                id=$( echo "$line" | cut -d $'\t' -f1 )
                title=$( echo "$line" | cut -d $'\t' -f3 )
                #echo "subcategory: $title"

		if grep -Fxq "$id" $subcat_list; then
			:
			#echo "visited category already"
		else
			#echo "going into subcat and writnig to file"
			echo "$id" >> $subcat_list
			title="$(echo -e "${title}" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')"
			srch=":"
			title=${title#*$srch}

			## calls self recursively on new subcategory if recurs true

			if [[ "$recurs" == "true" ]]; then
				./get_wiki_corpus_stage123.sh "$wiki_url" "$title" "$final_outfile" "$article_list" "$subcat_list" "$recurs"
			fi
		fi
	fi
done < "$outfile"


##clean up
rm $outfile $outputfile

exit
