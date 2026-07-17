let marks=[85,42,76,91,38,67,55,29,80,49];
let tp=0;
let tf=0;
for (let i=0;i<marks.length;i++ ){
    if(marks[i]>=50){
        // sconsole.log(`Student i: marks[i] - PASS`)
         console.log("Student: "+i+" "+marks[i]+" - PASS");
         tp++;
    }else{
        console.log("Student: "+i+" "+marks[i]+" - FAIL");
        tf++;
    }

}

console.log("Total Passed: "+tp);
console.log("Total Failed: "+tf)
