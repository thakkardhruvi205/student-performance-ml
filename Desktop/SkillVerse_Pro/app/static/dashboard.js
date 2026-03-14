const ctx = document.getElementById("skillChart");

new Chart(ctx, {

type: "bar",

data: {

labels: ["Python","Machine Learning","Web Dev","Cyber Security"],

datasets: [{

label: "Skill Level",

data: [90,75,85,65],

backgroundColor: [

"#6c8cff",
"#4caf50",
"#ff9800",
"#e91e63"

]

}]

},

options: {

responsive:true,

plugins:{
legend:{display:true}
}

}

});



const ctx2 = document.getElementById("progressChart");

new Chart(ctx2, {

type: "line",

data: {

labels:["Week1","Week2","Week3","Week4","Week5"],

datasets:[{

label:"Learning Progress",

data:[20,40,55,70,92],

borderColor:"#6c8cff",

fill:false,

tension:0.3

}]

},

options:{responsive:true}

});