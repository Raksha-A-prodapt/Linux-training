echo "Grade calculator"
echo
echo "Enter Subject 1: "
read a
echo "Enter Subject 2 : "
read b
echo "Enter Subject 3 : "
read c
echo "Enter Sub 4: "
read d
echo "Enter sub 5: "
read e
sum=$(( a + b + c + d + e ))
echo "Total: $sum"
avg=$((sum/5))
echo "Avg :$avg"
if [ $avg -ge 90 ]; then
   echo "Grade : A"
elif [ $avg -ge 75 ]; then
    echo "Grade : B"
elif [ $avg -ge 60 ]; then
    echo "Grade : C"
elif [ $avg -ge 50 ]; then
    echo "Grade : D"
else
   echo "fail"
fi
