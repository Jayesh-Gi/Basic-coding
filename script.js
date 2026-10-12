const employees = [
    { name: "Aman", salary: 25000 },
    { name: "Riya", salary: 40000 },
    { name: "Karan", salary: 18000 },
    { name: "Neha", salary: 35000 }
];
 for (let e of employees){
    if(e.salary >=25000){
        console.log(e.name)
    }
 }