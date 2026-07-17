let marks=[85,42,76,91,38,67,55,29,80,49];
let tp=0;
let tf=0;
let ts=0;
let tss=0
let ms=100;
let lss=0;
for (let i=0;i<marks.length;i++ ){
    if(marks[i]>=50){
        // sconsole.log(`Student i: marks[i] - PASS`)
         console.log("Student: "+i+" "+marks[i]+" - PASS");
         tp++;
        if(marks[i]>ts) {
            tss=i;
            ts=marks[i];
        }
    }else{
        console.log("Student: "+i+" "+marks[i]+" - FAIL");
        tf++;
        if(marks[i]<ms) {
            lss=i;
            ms=marks[i];
        }
        
    }

}

console.log("Total Passed: "+tp);
console.log("Total Failed: "+tf)

console.log(`Least scored by : ${lss} :${ms}`)
console.log(`Highest scored by : ${tss} :${ts}`)
