search_word(){
file=$1
word=$2
if grep -q "$word" "$file"  #qi
then
      echo "'$word' found in $file"
else
   echo "'$word' not found in $file"
fi
}

search_word file1.txt linux


count_word(){
file=$1
word=$2
count=$(grep -io "$word" "$file" | wc -l) #o
echo "occurance of $word: $count"
}

count_word file1.txt linux
# is the line where word is present
show_line(){
file=$1
word=$2

grep -n "$word - $file"
}

show_line file1.txt linux

