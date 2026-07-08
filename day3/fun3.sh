oddeve(){
if [[ $1%2 -eq 0 ]]; then # exce but why give 4(($1%2))
   echo "$1 is Even"
else 
   echo "$1 is Odd"
fi
}

echo "Enter Number: "
read n
oddeve n
