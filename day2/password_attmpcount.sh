user="admin"
password="Admin@123"
echo "Confirm your password: "

 for (( limit=1; limit<=3; limit++)); do
     echo "attemp $limit"
     read -s p2
     if [ "$password" == "$p2" ]; then 
           echo "loggedin successfully"
           exit 0
     fi
done 

echo  "Attempts finished! Try logging In Later!"
exit 1
