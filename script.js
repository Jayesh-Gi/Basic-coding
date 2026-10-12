const student = [
    { name: "Aman", marks: 85 },
    { name: "Rahul", marks: 72 },
    { name: "Priya", marks: 90 },
    { name: "Neha", marks: 65 }
    
];
for (let s of student){
    if (s.marks < 80){
        console.log(s.name);
    }
}
