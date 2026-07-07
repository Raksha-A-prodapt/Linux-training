echo "Enter user name: "
read a
echo "Set password(8 characters) "
password=""
while IFS=  read -r -s -n 1  char
do
   if [ -z "$char" ]; then
       break
   fi
   if [ ${#password} -lt 8 ]; then 
            password+="$char"
            printf "*"
  fi
done

echo

if [ ${#password} -ne 8 ]; then
   echo "password should strictly have exactly 8 chracters."
   exit 1
fi

if [[ "$password" =~ [A-Z] && \
      "$password" =~ [a-z] && \
      "$password" =~ [0-9] && \
      "$password" =~ [6a-zA-Z0-9] ]];
then 
  echo "password is valid"
else 
 echo "Entered password: $password"
 echo "invalid password."
 echo "Your password must me exactly 8 characters,with  atleast:"
 echo "-one uppercase"
 echo "-one loweecase"
 echo "-one special character"
 echo "-one numeric value"
 echo "password =$password"
 exit 1

fi

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
