extension="$1" #command line variable for the extension
for file in ./*."$extension"; do
        chmod u+x "$file"
done
