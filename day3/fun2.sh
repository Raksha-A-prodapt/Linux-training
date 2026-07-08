add_num(){
sum=$(( $1 + $2 ))  #here it should be  $1 for 1st arg, $2 for sec arg ... ts standard command
echo "sum = $sum"
}

echo "Enter num 1: "
read n1
echo "Enter num 2 : "
read n2

#add_num 10 20
add_num $n1 $n2
