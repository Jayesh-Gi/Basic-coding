const counter = {
    count: 0,

    increase:function(){
        this.count  = this.count+1;
        console.log(this.count)
    }
};

counter.increase();
counter.increase();
counter.increase();
