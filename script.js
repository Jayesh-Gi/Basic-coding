const name ={
    name: "Aman",
    salary: 30000,

    increaseSalary:function(){
        this.salary = this.salary+5000
        console.log(this.salary)
    }
} 
name.increaseSalary();