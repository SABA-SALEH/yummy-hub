/* jshint esversion: 6 */
var ingredientCounter = 1;
var ingredientCounter2 = 1;

/**
 * Function to add a new ingredient field dynamically
 */
function addIngredientField() {
    ingredientCounter++;
    // Create a new row for the ingredient
    var ingredientRow = document.createElement("div");
    ingredientRow.classList.add("row");
    // Create a field for the ingredient name
    var ingredientNameField = document.createElement("div");
    ingredientNameField.classList.add("col-md-6");
    ingredientNameField.innerHTML = `
        <div class="mb-3">
            <label for="ingredient_name_${ingredientCounter}" class="form-label"><i class="fas fa-shopping-basket"></i> Ingredient Name</label>
            <input type="text" class="form-control" id="ingredient_name_${ingredientCounter}" name="ingredient_name_${ingredientCounter}">
        </div>
    `;
    // Create a field for the ingredient quantity
    var ingredientQuantityField = document.createElement("div");
    ingredientQuantityField.classList.add("col-md-6");
    ingredientQuantityField.innerHTML = `
        <div class="mb-3">
            <label for="ingredient_quantity_${ingredientCounter}" class="form-label"><i class="fas fa-weight-hanging"></i> Ingredient Quantity</label>
            <input type="text" class="form-control" id="ingredient_quantity_${ingredientCounter}" name="ingredient_quantity_${ingredientCounter}">
        </div>
    `;

    ingredientRow.appendChild(ingredientNameField);
    ingredientRow.appendChild(ingredientQuantityField);

    var ingredientFieldsContainer = document.getElementById("ingredientFields");
    ingredientFieldsContainer.appendChild(ingredientRow);
}

/**
 * Function to add a new ingredient field (variant 2)
 */
function addIngredientField2() {
    var ingredientRow = document.createElement("div");
    ingredientRow.classList.add("row");

    var ingredientNameField = document.createElement("div");
    ingredientNameField.classList.add("col-md-6");
    ingredientNameField.innerHTML = '<div class="mb-3">' +
        '<label for="new_ingredient_name_' + ingredientCounter2 + '" class="form-label"><i class="fas fa-shopping-basket"></i> New Ingredient Name</label>' +
        '<input type="text" class="form-control" id="new_ingredient_name_' + ingredientCounter2 + '" name="new_ingredient_name">' +
        '</div>';

    var ingredientQuantityField = document.createElement("div");
    ingredientQuantityField.classList.add("col-md-6");
    ingredientQuantityField.innerHTML = '<div class="mb-3">' +
        '<label for="new_ingredient_quantity_' + ingredientCounter2 + '" class="form-label"><i class="fas fa-weight-hanging"></i> New Ingredient Quantity</label>' +
        '<input type="text" class="form-control" id="new_ingredient_quantity_' + ingredientCounter2 + '" name="new_ingredient_quantity">' +
        '</div>';

    ingredientRow.appendChild(ingredientNameField);
    ingredientRow.appendChild(ingredientQuantityField);

    var ingredientFieldsContainer = document.getElementById("ingredientFields");
    ingredientFieldsContainer.appendChild(ingredientRow);

    ingredientCounter2++;
}

/**
 * Function to validate the form before submission
 */
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

/**
 * Function to copy shareable link to clipboard
 */
function copyShareableLink() {
    const input = document.getElementById('shareableLink');
    input.select();
    document.execCommand('copy');
    alert('Shareable link copied to clipboard!');
}

/**
 * Function to handle category selection
 */
document.addEventListener("DOMContentLoaded", function () {
    var categorySelect = document.getElementById('categorySelect');
    var categoryForm = document.getElementById('categoryForm');
    // Event listener for category selection
    if (categorySelect && categoryForm) {
        categorySelect.addEventListener('change', function () {
            var category = this.value;
            console.log("Selected category:", category);
            // Construct the URL based on the selected category
            var baseUrl = categoryForm.getAttribute('data-base-url');
            var routeName = categoryForm.getAttribute('data-route-name');
            var url = baseUrl + "/" + category;

            categoryForm.action = url;
            categoryForm.submit();
        });
    }
    // Event listener for delete comment button
    document.addEventListener("click", function (event) {
        if (event.target && event.target.classList.contains("delete-comment")) {
            var button = event.target;
            var commentId = button.dataset.commentId;
            var formAction = "/delete_comment/" + commentId;
            document.getElementById("deleteCommentForm").setAttribute("action", formAction);
            var bsModal = new bootstrap.Modal(document.getElementById("confirmDeleteModal"));
            bsModal.show();
        }
    });
});

/**
 * Function to print the recipe details
 */
function printRecipe() {

    var recipeDetails = document.getElementById('recipe-details');
    var printWindow = window.open('', '_blank');
    // Write the recipe details to the print window
    printWindow.document.write('<html><head><title>Recipe Details</title></head><body>');
    printWindow.document.write(recipeDetails.innerHTML);
    printWindow.document.write('</body></html>');

    printWindow.document.close();
    printWindow.print();
}