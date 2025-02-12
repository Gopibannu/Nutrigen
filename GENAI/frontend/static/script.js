function getDietPlan() {
    let weight = document.getElementById("weight-input").value;
    let goal = document.getElementById("goal").value;
    let dietType = document.getElementById("diet-type").value;

    fetch("/get_diet_plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ weight, goal, dietType })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("diet-results").innerHTML = JSON.stringify(data.diet_plan, null, 2);
    });
}

function getNutrition() {
    let food = document.getElementById("food-input").value;
    
    fetch("/get_nutrition", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ food })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("nutrition-results").innerHTML = JSON.stringify(data, null, 2);
    });
}
