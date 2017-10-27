a=1950
for i in *.csv; do
  new=$(printf "%01d.csv" "$a") 
  mv -i -- "$i" "$new"
  let a=a+1
done
