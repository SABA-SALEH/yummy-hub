var ingredientCounter = 1;

function addIngredientField() {
    ingredientCounter++;


    var ingredientNameField = document.createElement("div");
    ingredientNameField.classList.add("mb-3");
    ingredientNameField.innerHTML = `
            <label for="ingredient_name_${ingredientCounter}" class="form-label">Ingredient Name</label>
            <input type="text" class="form-control" id="ingredient_name_${ingredientCounter}" name="ingredient_name_${ingredientCounter}">
        `;


    var ingredientQuantityField = document.createElement("div");
    ingredientQuantityField.classList.add("mb-3");
    ingredientQuantityField.innerHTML = `
            <label for="ingredient_quantity_${ingredientCounter}" class="form-label">Ingredient Quantity</label>
            <input type="text" class="form-control" id="ingredient_quantity_${ingredientCounter}" name="ingredient_quantity_${ingredientCounter}">
        `;


    var ingredientFieldsContainer = document.getElementById("ingredientFields");
    ingredientFieldsContainer.appendChild(ingredientNameField);
    ingredientFieldsContainer.appendChild(ingredientQuantityField);
}




var ingredientCounter2 = 1;



function addIngredientField2() {
    var ingredientNameField = document.createElement("div");
    ingredientNameField.classList.add("mb-3");
    ingredientNameField.innerHTML = '<label for="new_ingredient_name_' + ingredientCounter2 + '" class="form-label">New Ingredient Name</label>' +
        '<input type="text" class="form-control" id="new_ingredient_name_' + ingredientCounter2 + '" name="new_ingredient_name">';

    var ingredientQuantityField = document.createElement("div");
    ingredientQuantityField.classList.add("mb-3");
    ingredientQuantityField.innerHTML = '<label for="new_ingredient_quantity_' + ingredientCounter2 + '" class="form-label">New Ingredient Quantity</label>' +
        '<input type="text" class="form-control" id="new_ingredient_quantity_' + ingredientCounter2 + '" name="new_ingredient_quantity">';

    var ingredientFieldsContainer = document.getElementById("ingredientFields");
    ingredientFieldsContainer.appendChild(ingredientNameField);
    ingredientFieldsContainer.appendChild(ingredientQuantityField);

    ingredientCounter2++;
}



function validateForm() {
    var title = document.getElementById("title").value;
    var description = document.getElementById("description").value;
    var instructions = document.getElementById("instructions").value;
    var preparationTime = document.getElementById("preparation_time").value;
    var cookTime = document.getElementById("cook_time").value;
    var imageUrl = document.getElementById("image_url").value;
    var category = document.getElementById("category").value;

    if (title.trim() === "" || description.trim() === "" || instructions.trim() === "" || preparationTime.trim() === "" || cookTime.trim() === "" || imageUrl.trim() === "" || category.trim() === "") {
        alert("Please fill out all required fields.");
        return false;
    }

    return true;
}


