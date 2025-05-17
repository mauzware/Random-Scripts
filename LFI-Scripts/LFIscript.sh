while IFS="" read -r p || [ -n "$p" ]
do
  printf '%s\n' "$p"
  curl 'http://{DOMAIN}/script.php?page='"$p"
done < paths.txt
