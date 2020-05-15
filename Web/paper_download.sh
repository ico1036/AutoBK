cat paper_url.txt | while read line
do
	wget $line
done
