mkdir recover
touch files.txt recover.txt
cp ./looping.sh ./mission
mv  recover.txt deleted.txt
find . -name "files.txt"
chmod +x files.txt
tar -cvf recover.tar programs/
mv recover.tar /project1
ls



