echo '1'
extension="$1"
echo "$extension"
for file in ./*."$extension"; do
   chmod u+x "$file"
  echo "$file"

done;

